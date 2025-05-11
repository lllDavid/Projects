import socket
from service import Service
from threading import Thread


class Server:
    def __init__(self):
        self.user_instance = Service()

    def start_server(self, host="0.0.0.0", port=1234):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)  
        print("Server started")
        print(f"Running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            t = Thread(target=self.handle_client, args=(conn, addr))
            t.start()

    def handle_client(self, conn, addr):
        print(f"New connection: {addr[0]}")

        while True:
            try:
                user_data = conn.recv(1024)
                user_message = user_data.decode().strip()

                match user_message:
                    case "1":
                        self.user_instance.image_recognition(conn, addr)
                    case "2":
                        self.user_instance.ftp_recognition(conn)
        
            except Exception as e:
                print(f"Error while handling client {addr}: {e}")
                break

        conn.close()
        print(f"Connection from {addr} closed.")

if __name__ == "__main__":
    server = Server()
    server.start_server()
