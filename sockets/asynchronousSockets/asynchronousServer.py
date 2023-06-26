import asyncio

HOST = 'localhost'
PORT = 8000
num_clients = 0


async def handle_client(reader, writer):
    global num_clients
    data = await reader.read(4096)
    if data:
        login_message = "Logged In"
        writer.write(login_message.encode())
        await writer.drain()
        num_clients += 1
        # print(f"{num_clients} -> {data.decode()}")
        while True:
            data = await reader.read(4096)
            if data:
                print(data.decode()[:5])
            # packet_count += 1
            # print(f'{packet_count} Received packet {data}')

    # print(f'Total packets received: {packet_count}')
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, HOST, PORT)
    print(f'Server listening on {HOST}:{PORT}...')

    async with server:
        await server.serve_forever()


asyncio.run(main())
