import socket
import select

HOST = 'localhost'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f'Server listening on {HOST}:{PORT}...')

    # Make the server socket non-blocking
    s.setblocking(False)

    inputs = [s]
    packet_count = 0

    while True:
        # Use select to wait for data from any socket
        read_sockets, _, _ = select.select(inputs, [], [])

        for sock in read_sockets:
            # If the socket is the server socket, accept the connection
            if sock == s:
                conn, addr = s.accept()
                print(f'Connected by {addr}')
                conn.setblocking(False)
                inputs.append(conn)
            # If the socket is a client socket, receive data
            else:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    inputs.remove(sock)
                else:
                    packet_count += 1
                    print(f'Received packet {packet_count}')

        # Check for any closed client sockets and remove them from the inputs list
        for sock in inputs:
            if sock.fileno() == -1:
                inputs.remove(sock)

        # Exit the loop if all client sockets are closed
        if len(inputs) == 1:
            break

    print(f'Total packets received: {packet_count}')
