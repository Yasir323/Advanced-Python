"""
A prototype message broker.
"""

import asyncio
from asyncio import StreamWriter, StreamReader, gather
from collections import deque, defaultdict
from typing import Deque, DefaultDict

from msgproto import read_msg, send_msg  # 1

SUBSCRIBERS: DefaultDict[bytes, Deque] = defaultdict(deque)  # 2
# SUBSCRIBERS = {'channel_name': [<list of subscribers>]}


async def client(reader: StreamReader, writer: StreamWriter) -> None:
    peer_name = writer.get_extra_info('peername')  # 3
    subscribe_channel = await read_msg(reader)  # 4
    SUBSCRIBERS[subscribe_channel].append(writer)  # 5
    print(f'Remote {peer_name} subscribed to {subscribe_channel}')
    try:
        while channel_name := await read_msg(reader):  # 6
            data = await read_msg(reader)  # 7
            print(f'Sending to {channel_name}: {data[:19]}...')
            conns = SUBSCRIBERS[channel_name]  # 8
            if conns and channel_name.startswith(b'/queue'):  # 9
                conns.rotate()  # 10
                conns = [conns[0]]  # 11
            await gather(*[send_msg(c, data) for c in conns])  # 12
    except asyncio.CancelledError:
        print(f'Remote {peer_name} closing connection.')
        writer.close()
        await writer.wait_closed()
    except asyncio.IncompleteReadError:
        print(f'Remote {peer_name} disconnected')
    finally:
        print(f'Remote {peer_name} closed')
        SUBSCRIBERS[subscribe_channel].remove(writer)  # 13


async def main(*args, **kwargs) -> None:
    server = await asyncio.start_server(*args, **kwargs)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main(client, host='127.0.0.1', port=25000))
    except KeyboardInterrupt:
        print('Bye!')


"""
1. Imports from our msgproto.py module.

2. A global collection of currently active subscribers. Every time a client
connects, they must first send a channel name they’re subscribing to. A
deque will hold all the subscribers for a particular channel.

3. The client() coroutine function will produce a long-lived coroutine for
each new connection. Think of it as a callback for the TCP server started
in main(). On this line, I’ve shown how the host and port of the remote
peer can be obtained, for example, for logging.

4. Our protocol for clients is the following:
On first connect, a client must send a message containing the channel to
subscribe to (here, subscribe_chan).
Thereafter, for the life of the connection, a client sends a message to a
channel by first sending a message containing the destination channel name,
followed by a message containing the data. Our broker will send such data
messages to every client subscribed to that channel name.

5. Add the StreamWriter instance to the global collection of subscribers.

6. An infinite loop, waiting for data from this client. The first message
from a client must be the destination channel name.

7. Next comes the actual data to distribute to the channel.

8. Get the deque of subscribers on the target channel.

9. Some special handling if the channel name begins with the magic word
/queue: in this case, we send the data to only one of the subscribers,
not all of them. This can be used for sharing work between a bunch of
workers, rather than the usual pub-sub notification scheme, where all
subscribers on a channel get all the messages.

10. Here is why we use a deque and not a list: rotation of the deque is
how we keep track of which client is next in line for /queue distribution.
This seems expensive until you realize that a single deque rotation is
an O(1) operation.

11. Target only whichever client is first; this changes after every rotation.

12. Create a list of coroutines for sending the message to each writer,
and then unpack these into gather() so we can wait for all of the sending
to complete.
This line is a bad flaw in our program, but it may not be obvious why:
though it may be true that all of the sending to each subscriber will
happen concurrently, what happens if we have one very slow client? In
this case, the gather() will finish only when the slowest subscriber
has received its data. We can’t receive any more data from the sending
client until all these send_msg() coroutines finish. This slows all
message distribution to the speed of the slowest subscriber.

13. When leaving the client() coroutine, we make sure to remove ourselves
from the global SUBSCRIBERS collection. Unfortunately, this is an O(n)
operation, which can be a little expensive for very large n. A different
data structure would fix this, but for now we console ourselves with the
knowledge that connections are intended to be long-lived—thus, there
should be few disconnection events—and n is unlikely to be very large
(say ~10,000 as a rough order-of-magnitude estimate), and this code is at
least easy to understand.
"""
