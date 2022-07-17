import asyncio

"""
Here you can see that the exception handler for CancelledError was triggered. Now
let’s imagine that this is a real-world production application, and we want to send all
events about dropped connections to a monitoring service.
"""


async def send_event(msg: str):
    await asyncio.sleep(1)


async def echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("New Connection.")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("Leaving connection.")
    except asyncio.CancelledError:
        msg = "Connection dropped!"
        print(msg)
        asyncio.create_task(send_event(msg))
        """
        Because the event notifier involves network access, it is common for such
        calls to be made in a separate async task; that’s why we’re using the
        create_task() function here.
        """


async def main(host="127.0.0.1", port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye!")

"""
This code has a bug, however. It becomes obvious if we rerun the example, and make
sure to stop the server (with Ctrl-C) while a connection is active.

To understand why this is happening, we must go back to the sequence of cleanup
events that asyncio.run() does during the shutdown phase; in particular, the important
part is that when we press Ctrl-C, all the currently active tasks are collected and
cancelled. At this point, only those tasks are then awaited, and asyncio.run() returns
immediately after that. The bug in our modified code is that we created a new task
inside the cancellation handler of our existing “echo” task. This new task was created
only after asyncio.run() had collected and cancelled all the tasks in the process.

As a general rule of thumb, try to avoid creating new tasks inside
CancelledError exception handlers. If you must, be sure to also
await the new task or future inside the scope of the same function.
"""
