from socket import *

server = {
    'ip': '127.0.0.1',
    'port': 6543
}

with socket(AF_INET, SOCK_STREAM) as object_socket:
    object_socket.bind((server['ip'], server['port']))
    object_socket.listen(3)
    print(f'Listening on {server["ip"]}:{server["port"]}')

    print('Awaiting client...')
    connection, client = object_socket.accept()

    with connection:
        print(f'Connected with {client[0]}:{client[1]}')
        while True:
            message_received = str(bytes(connection.recv(1024)), 'utf-8')
            print(f'Received: {message_received}')
            if not message_received:
                break
            connection.sendall(b'Read confirmation.')
