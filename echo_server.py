import socket

# preset bytes to read value, and host address, and port number
BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080


def handle_connection(conn, addr):
    # conn is a socket, directly to the client created by the s.accept function
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                break
            print(data)
            conn.sendall(data)


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        # allows rebind to same address
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        s.listen()

        conn, addr = s.accept()
        handle_connection(conn, addr)


start_server()
