import asyncio
import random

HOST = 'localhost'
PORT = 8000
NUM_CLIENTS = 5000
PACKETS_PER_CLIENT = 1
packets_sent = 0
byte_array = [0x00, 0x00, 0x01, 0x05, 0x78, 0x78, 0x11, 0x01, 0x08, 0x63, 0x55, 0x20, 0x40, 0x08, 0x55, 0x87, 0x20,
              0x03, 0x00, 0x01, 0x01, 0xaf, 0x00, 0x71, 0x0d, 0x0a]


async def send_packets(writer: asyncio.StreamWriter):
    global packets_sent
    for i in range(PACKETS_PER_CLIENT):
        packet = f'Packet {i + 1}'
        writer.write(packet.encode())
        await writer.drain()
        packets_sent += 1
        # await asyncio.sleep(random.uniform(0.1, 0.5))

    writer.close()


async def main():
    tasks = []

    for i in range(NUM_CLIENTS):
        reader, writer = await asyncio.open_connection(HOST, PORT)
        task = asyncio.create_task(send_packets(writer))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print("Packets sent:", packets_sent)


asyncio.run(main())

