from classifier import Classifier
from ftplib import FTP

class User:
    def __init__(self):
        self.user_data = {}

    def register(self, conn, addr):
        new_username = conn.recv(1024).decode()
        new_password = conn.recv(1024).decode()

        if new_username and new_password:
            if new_username not in self.user_data:
                self.user_data[new_username] = new_password
                conn.sendall("You have been registered.\n".encode())
                print(f"[{new_username}] registered with IP: [{addr[0]}]")
            else:
                conn.sendall("Username already exists\n".encode())
        else:
            conn.sendall("Username and password cannot be empty\n".encode())

    def login(self, conn, addr):
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()

        if username in self.user_data and self.user_data[username] == password:
            conn.sendall(f"Welcome {username}.\n".encode())
            print(f"[{username}] logged in with IP: [{addr[0]}]")
        else:
            conn.sendall("Wrong credentials.".encode())
            print(f"{addr[0]} tried to log in with username: {username} and password: {password}")

    def handle_user_contact_message(self, conn, addr):
        user_message = conn.recv(1024).decode()
        print(f"[{self.username}] sent the message: [{user_message}] with IP: [{addr[0]}]")
        conn.sendall(f"{addr[0]} we received your message.\n".encode())

    def run_image_recognition(self, conn, image_path=None):
        ftp_yes_no = conn.recv(1024).decode().strip()

        if ftp_yes_no == "Y":
            username = conn.recv(1024).decode()
            password = conn.recv(1024).decode()

            self.connect_to_ftp(conn, username, password)
            print("Uploading file...")

            image_path = self.upload_file(conn)

            if image_path is None:
                print("File upload failed.")
                return

            c = Classifier()
            result = c.main(image_path)
            conn.sendall(f"Result: {result}".encode())
            print("Result sent to client.")

        elif ftp_yes_no == "N":
            image_path = conn.recv(1024).decode()
            print("Performing image recognition...")

            c = Classifier()
            result = c.main(image_path)
            conn.sendall(f"Result: {result}".encode())
            print("Result sent to client.")

    def connect_to_ftp(self, conn, username, password, host="127.0.0.1"):
        self.ftp = FTP(host)
        self.ftp.login(username, password)

    def upload_file(self, conn):
        conn.send(b"Please send the file path to upload:")
        file_path = conn.recv(1024).decode()
        normalized_filename = file_path.replace('\\', '/')
    
        try:
            conn.send(b"File uploaded successfully!")
            return normalized_filename 
        except Exception as e:
            conn.send(f"Failed to upload file: {str(e)}".encode())
            return None
    
    def reset():
        pass

    def delete():
        pass



    

    

   