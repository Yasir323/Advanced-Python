import socket
import threading
import time

HOST = '10.5.50.4'
PORT = 8000
NUM_CLIENTS = 1
PACKETS_PER_CLIENT = 5
MESSAGE = b'2929800028ABCD0000150314234153026368560793189500000394F88FD18FFFFF0000001E0000000000000A0D'
PACKETS_SENT = NUM_CLIENTS * PACKETS_PER_CLIENT


def send_packets():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        for i in range(PACKETS_PER_CLIENT):
            s.sendall(MESSAGE)
            print(s.recv(1024))


# Create threads for each client
threads = []
for i in range(NUM_CLIENTS):
    t = threading.Thread(target=send_packets)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()

print(f'Total packets sent: {PACKETS_SENT}')
