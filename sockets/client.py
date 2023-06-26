import socket

mysock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/ HTTP/1.0\r\n\r\n'.encode('utf-8')
mysock.send(cmd)

while True:
    try:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end='')
    except KeyboardInterrupt:
        break
mysock.close()
