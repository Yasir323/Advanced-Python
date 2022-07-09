from threading import stack_size
from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor

"""
When using a large number of threads we can limit the
size of the virtual memory the program is using by using
threading.stack_size().
"""
stack_size(65536)


def echo_client(sock, client_addr):
    """
    Handle a client connection.
    """
    print("Got a connection from: ", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection.")
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


echo_server(('', 15_000))
