import socket
from typing import *


def algorithm(n: int) -> int:
    return n + 42

def handler(client: socket.socket) -> None:
    while True:
        request: bytes = client.recv(100)
        if not request.strip():
            client.close()
            return
        number = int(request)
        result = algorithm(number)
        client.send(f'{result}\n'.encode('ascii'))
    
Address = Tuple[str, int]
def server(address: Address) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)

    while True:
        client, addr = sock.accept()
        print(f'Connection from {addr}')
        handler(client)

server(('localhost', 30303))