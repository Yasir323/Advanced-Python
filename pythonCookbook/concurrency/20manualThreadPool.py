from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
from queue import Queue


def echo_client(q):
    """
    Handle a client connection.
    """
    sock, client_addr = q.get()
    print("Got a connection from: ", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection.")
    sock.close()


def echo_server(addr, n_workers):
    q = Queue()
    for i in range(n_workers):
        thread = Thread(target=echo_client, args=(q,), daemon=True)
        thread.start()

    # Run the server
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))


echo_server(('', 15_000), 128)
