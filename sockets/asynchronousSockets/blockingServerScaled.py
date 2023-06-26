import socket
import threading

HOST = 'localhost'
PORT = 8000
packet_count = 0

def handle_client(conn, addr):
    global packet_count

    while True:
        data = conn.recv(1024)
        if not data:
            break
        packet_count += 1
        print(f'Received packet {packet_count} from {addr}')

    print(f'Total packets received from {addr}: {packet_count}')
    conn.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    # Note that we set the backlog argument of the
    # s.listen() method to a large value (1024 in
    # this example) to allow a large number of
    # clients to queue up while waiting for a connection.
    s.listen(1024)
    print(f'Server listening on {HOST}:{PORT}...')

    while True:
        conn, addr = s.accept()
        print(f'Connected by {addr}')
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
