import socket

_IP = "127.0.0.1"
_PORT = 12321
bufferSize = 512
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind((_IP, _PORT))
print(f"-----------Listening on {_IP}:{_PORT}")

while True:
    data, addr = sock.recvfrom(bufferSize)
    print(data.decode(), end='')
