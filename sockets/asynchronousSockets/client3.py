import socket
from concurrent.futures import ThreadPoolExecutor
import time
import threading

HOST = '10.5.50.4'
PORT = 8000
NUM_CLIENTS = 10
PACKETS_PER_CLIENT = 5
MESSAGE = b'2929800028ABCD0000150314234153026368560793189500000394F88FD18FFFFF0000001E0000000000000A0D'
PACKETS_SENT = NUM_CLIENTS * PACKETS_PER_CLIENT
lock = threading.Lock()


def send_packets():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        received = []
        for i in range(PACKETS_PER_CLIENT):
            s.sendall(MESSAGE)
            received.append(s.recv(1024))
        with lock:
            print(f"{threading.current_thread().native_id} -> {len(received)}")


# Create threads for each client
with ThreadPoolExecutor(1024) as executor:
    threads = [executor.submit(send_packets) for _ in range(NUM_CLIENTS)]

print(f'Total packets sent: {PACKETS_SENT}')
