import socket

class Client:
    def __init__(self, host="127.0.0.1", port=1234):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.client_socket.connect((self.host, self.port))
        print(f"Connected to {self.host}.")

    def send_request(self, user_input):
        self.client_socket.sendall(user_input.encode())

    def handle_image_recognition(self):
        image_path = input("Enter image path(eg. images\\dog.12492.jpg):")
        self.send_request(image_path)
        server_response = self.client_socket.recv(1024).decode()
        print(server_response)

    def handle_ftp_recognition(self):
        ftp_username = input("Enter username for FTP: ")
        self.send_request(ftp_username)
        ftp_password = input("Enter password for FTP: ")
        self.send_request(ftp_password)

        server_response = self.client_socket.recv(1024).decode()
        if server_response == "Ok":
            image_path = input("Enter image path(eg. C:\\FTP\\dog.12492.jpg):")
            self.send_request(image_path)
            server_response = self.client_socket.recv(1024).decode()
            print(server_response)

        server_response = self.client_socket.recv(1024).decode()
        print(server_response)

    def choices(self):
        while True:
            user_input = input("[1] Image Recognition\n[2] Image Recognition(FTP)\n[3] To exit\n")
            
            match user_input:
                case "3":
                    break
                case "1":
                    self.send_request(user_input)
                    self.handle_image_recognition()
                case "2":
                    self.send_request(user_input)
                    self.handle_ftp_recognition()
                case _:
                    print(f"{user_input} is not a valid input.\n")

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = Client()
    client.connect()
    client.choices()
    client.close()
