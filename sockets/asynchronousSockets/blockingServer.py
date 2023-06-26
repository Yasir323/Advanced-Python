import socket

HOST = 'localhost'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f'Server listening on {HOST}:{PORT}...')

    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        packet_count = 0

        while True:
            data = conn.recv(1024)
            if not data:
                break
            packet_count += 1
            print(f'Received packet {packet_count}')

        print(f'Total packets received: {packet_count}')
