import socket

def client():
    host = "127.0.0.1"
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    print(f"Connected to {host}.")

    while True:
        user_input = input("Press Enter to list options or type 'quit' to exit: ")
        
        if user_input.lower() == "quit":
            print("Exiting.")
            break
        
        if user_input == "":
            user_input = input("[1] Register\n[2] Login\n[3] Image Recognition\n[4] Contact\n")

        if user_input in ["1", "2", "3", "4"]:
            client_socket.sendall(user_input.encode())

            if user_input == "1":
                username = input("Choose a username: ")
                client_socket.sendall(username.encode())
                password = input("Choose a password: ")
                client_socket.sendall(password.encode())

                server_response = client_socket.recv(1024).decode()
                print(server_response)

            elif user_input == "2":
                username = input("Enter username: ")
                client_socket.sendall(username.encode())
                password = input("Enter password: ")
                client_socket.sendall(password.encode())

                server_response = client_socket.recv(1024).decode()
                print(server_response)

            elif user_input == "3":
                ftp = input("Upload image via FTP ? (Y/N)")
                if ftp == "Y":
                    client_socket.sendall(ftp.encode())
                    ftp_username = input("Enter username for FTP: ")
                    client_socket.sendall(ftp_username.encode())
                    ftp_password = input("Enter password for FTP: ")
                    client_socket.sendall(ftp_password.encode())

                    server_response = client_socket.recv(1024).decode()
                    if server_response == "Please send the file path to upload:":
                        image_path = input("Enter image path: ")
                        client_socket.sendall(image_path.encode())
                        server_response = client_socket.recv(1024).decode()
                        print(server_response)
                        
                elif ftp == "N":
                    client_socket.sendall(ftp.encode())
                    image_path = input("Enter image path(eg. images/dog.12492.jpg):")
                    client_socket.sendall(image_path.encode())
                
                server_response = client_socket.recv(1024).decode()
                print(server_response)

            elif user_input == "4":
                user_message = input("Enter message: ")
                client_socket.sendall(user_message.encode())

                server_response = client_socket.recv(1024).decode()
                print(server_response)

            else:
                print(f"{user_input} is not a valid input.\n")

    client_socket.close()

client()
