import asyncio

NUM_CLIENTS = 5000
HOST = "127.0.0.1"
PORT = 8000
counter = 0


async def send_packets(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    global counter
    login_message = login_messages.pop()
    writer.write(login_message.encode())
    await writer.drain()
    ack = await reader.read(1024)
    counter += 1
    # print(f"Client - {counter} Received: {ack.decode()}")
    while True:
        location_data = "787822221702150a3b25cf0333542f0861c3ef0014e8019462160a0002af010e0004aa20970d0a787822221702150b2425cf033354ec0861c3d00014e8019462160a0002af010e0004aa20970d0a787822221702150b2716cf033354580861c35f0014e8019462160a0002af010e0004aa20970d0a787822221702150b2d25cf033354600861c4200014e8019462160a0002af010e0004aa20970d0a787822221702150b3234cf033354ab0861c34f0014e8019462160a0002af010e0004aa20970d0a787822221702150c0607cf033353330861c58f0014e8019462160a0002af010e0004aa20970d0a787822221702150c0616cf033353700861c6a00014e8019462160a0002af010e0004aa20970d0a787822221702150c0625cf033354940861c62f0014e8019462160a0002af010e0004aa20970d0a787822221702150c0634cf033355340861c5700014e8019462160a0002af010e0004aa20970d0a787822221702150c0716cf033355830861c4600014e8019462160a0002af010e0004aa20970d0a "
        writer.write(location_data.encode())
        await writer.drain()
        await asyncio.sleep(1)
    # writer.close()


async def main():
    tasks = []

    for i in range(NUM_CLIENTS):
        reader, writer = await asyncio.open_connection(HOST, PORT)
        task = asyncio.create_task(send_packets(reader, writer))
        tasks.append(task)
    await asyncio.gather(*tasks)

login_messages = []
with open("loginMessages.txt") as fd:
    for line in fd.readlines():
        login_messages.append(line.strip())
asyncio.run(main())
