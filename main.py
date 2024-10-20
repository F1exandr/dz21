import socket

def start_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Сервер слушает на {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Соединение от {address}")

        data = client_socket.recv(1024)
        print(f"Получены данные: {data.decode()}")

        response = "Привет, клиент!"
        client_socket.sendall(response.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()