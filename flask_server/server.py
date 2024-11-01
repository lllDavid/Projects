import user
import socket
import threading

class Server:
    def __init__(self):
        self.user_instance = user.User()
        self.active_connections = []    

    def start_server(self, host="0.0.0.0", port=1234):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(5)  
        print("Server started")
        print(f"Running on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            t = threading.Thread(target=self.handle_client, args=(conn, addr))
            t.start()

    def handle_client(self, conn, addr):
        print(conn.recv(1024).decode())
        print(f"New connection: {addr[0]}")
        self.active_connections.append(addr[0])

        while True:
            try:
                user_data = conn.recv(1024)
                user_message = user_data.decode().strip()

                match user_message:
                    case "1":
                        self.user_instance.register(conn, addr)
                    case "2":
                        self.user_instance.login(conn, addr)
                    case "3":
                        self.user_instance.run_image_recognition(conn)
                    case "4":
                        self.user_instance.handle_user_contact_message(conn)

            except Exception as e:
                print(f"Error while handling client {addr}: {e}")
                break

        conn.close()
        print(f"Connection from {addr} closed.")

if __name__ == "__main__":
    server = Server()
    server.start_server()
