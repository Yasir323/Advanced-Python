"""
Sender: a toolkit for sending data to our message broker
"""

import asyncio
import argparse
import uuid
from itertools import count

from msgproto import send_msg


async def main(args):
    me = uuid.uuid4().hex[:8]  # 1
    print(f"Starting up {me}")
    reader, writer = await asyncio.open_connection(
        host=args.host,
        port=args.port
    )  # 2
    print(f"I am {writer.get_extra_info('sockname')}")
    channel = b'/null'  # 3
    await send_msg(writer, channel)  # 4
    chan = args.channel.encode()  # 5
    try:
        for i in count():  # 6
            await asyncio.sleep(args.interval)  # 7
            data = b'X'*args.size or f"Msg {i} from {me}".encode()
            try:
                await send_msg(writer, chan)
                await send_msg(writer, data)  # 8
            except OSError:
                print("Connection ended.")
                break
    except asyncio.CancelledError:
        writer.close()
        await writer.wait_closed()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # 9
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=25000, type=int)
    parser.add_argument('--channel', default='/topic/foo')
    parser.add_argument('--interval', default=1, type=float)
    parser.add_argument('--size', default=0, type=int)
    try:
        asyncio.run(main(parser.parse_args()))
    except KeyboardInterrupt:
        print('Bye!')


"""
1. As with the listener, claim an identity.

2. Reach out and make a connection.

3. According to our protocol rules, the first thing to do after connecting to the
server is to give the name of the channel to subscribe to; however, since we are a
sender, we don’t really care about subscribing to any channels. Nevertheless, the
protocol requires it, so just provide a null channel to subscribe to (we won’t
actually listen for anything).

4. Send the channel to subscribe to.

5. The command-line parameter args.channel provides the channel to which we
want to send messages. It must be converted to bytes first before sending.

6. Using itertools.count() is like a while True loop, except that we get an iteration
variable to use. We use this in the debugging messages since it makes it a bit
easier to track which message got sent from where.

7. The delay between sent messages is an input parameter, args.interval. The next
line generates the message payload. It’s either a bytestring of specified size
(args.size) or a descriptive message. This flexibility is just for testing.

8. Note that two messages are sent here: the first is the destination channel name,
and the second is the payload.

9. As with the listener, there are a bunch of command-line options for tweaking the
sender: channel determines the target channel to send to, while interval controls
the delay between sends. The size parameter controls the size of each message payload.
"""
