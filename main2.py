import socket

def start_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))
    print(f"Соединение с {host}:{port}")

    data = "Привет, сервер!"
    client_socket.sendall(data.encode())

    response = client_socket.recv(1024)
    print(f"Получен ответ: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    start_client()