from ftplib import FTP
from classifier import Classifier

class Service:
    def image_recognition(self, conn, image_path=None):
        image_path = conn.recv(1024).decode()
        normalized_imagename = image_path.replace('\\', '/')
        print("Performing image recognition...")

        c = Classifier()
        result = c.main(normalized_imagename)
        conn.sendall(f"Result: {result}".encode())
        print("Result sent to client.")
    
    def ftp_connection(self, conn, username, password, host="127.0.0.1"):
        self.ftp = FTP(host)
        self.ftp.login(username, password)

    def ftp_upload(self, conn):
        conn.send(b"Ok")
        file_path = conn.recv(1024).decode()
        normalized_filename = file_path.replace('\\', '/')
    
        try:
            conn.send(b"File uploaded successfully!")
            return normalized_filename 
        except Exception as e:
            conn.send(f"Failed to upload file: {str(e)}".encode())
            return None

    def ftp_recognition(self, conn):
        username = conn.recv(1024).decode()
        password = conn.recv(1024).decode()

        self.ftp_connection(conn, username, password)

        image_path = self.ftp_upload(conn)

        if image_path is None:
            print("File upload failed.")
            return

        print("Performing image recognition...")
        c = Classifier()
        result = c.main(image_path)
        conn.sendall(f"Result: {result}".encode())
        print("Result sent to client.")

