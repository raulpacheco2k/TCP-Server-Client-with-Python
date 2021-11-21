from socket import *

server = {
    'ip': '127.0.0.1',
    'port': 6543
}


with socket(AF_INET, SOCK_STREAM) as object_socket:
    object_socket.connect((server['ip'], server['port']))

    while True:
        message = bytes(input('Message: '), 'utf-8')
        if not message:
            break
        object_socket.send(message)
        answer = object_socket.recv(1024)
        print(answer)
