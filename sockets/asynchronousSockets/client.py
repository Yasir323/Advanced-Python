import socket
import threading
import time

HOST = '10.5.50.4'
PORT = 8000
NUM_CLIENTS = 5
PACKETS_PER_SECOND = 2
MESSAGE = b'Hello, server!'
PACKETS_SENT = NUM_CLIENTS * PACKETS_PER_SECOND


def send_packets():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        packets_sent = 0

        while packets_sent < PACKETS_SENT:
            for i in range(PACKETS_PER_SECOND):
                s.sendall(MESSAGE)
                packets_sent += 1
                print(s.recv(1024))
            time.sleep(1/PACKETS_PER_SECOND)

        print(f'Total packets sent: {packets_sent}')


# Create threads for each client
threads = []
for i in range(NUM_CLIENTS):
    t = threading.Thread(target=send_packets)
    t.start()
    threads.append(t)

# Wait for all threads to finish
for t in threads:
    t.join()
