import asyncio


async def echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("New Connection.")
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print("Leaving connection.")
    except asyncio.CancelledError:
        print("Connection dropped!")


async def main(host="127.0.0.1", port=8888):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye!")
