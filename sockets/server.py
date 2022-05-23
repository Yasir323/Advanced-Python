import socket


def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(('localhost', 9000))
        server_socket.listen(5)
        while True:
            (client_socket, address) = server_socket.accept()
            decoded_request = client_socket.recv(5000).decode()
            pieces = decoded_request.split('\n')
            if len(pieces) > 0:
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            client_socket.sendall(data.encode())
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as e:
        print("Error:\n")
        print(e)

    server_socket.close()

print("Access http:localhost:9000")
create_server()
