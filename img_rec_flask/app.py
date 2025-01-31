from flask import Flask, render_template, request, session, redirect
import socket

app = Flask(__name__)

host = "127.0.0.1"
port = 1234

app.secret_key = 'your_secret_key'

def communicate_with_server(user_choice, ftp_choice, ftp_username=None, ftp_password=None, image_path=None):
    response_message = ''
    
    try:
        if 'client_socket' in session:
            client_socket = session['client_socket']
        else:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            session['client_socket_connected'] = True
            
        print("Successfully connected to the server.")
        
        client_socket.sendall(user_choice.encode())
        
        if user_choice == "3":
            client_socket.sendall(ftp_choice.encode())
            
            if ftp_choice == "Y":
                client_socket.sendall(ftp_username.encode())
                client_socket.sendall(ftp_password.encode())

                response_message = client_socket.recv(1024).decode()

                if response_message == "Please send the file path to upload:":
                    client_socket.sendall(image_path.encode())
                    response_message = client_socket.recv(1024).decode()
            elif ftp_choice == "N":
                client_socket.sendall(image_path.encode())
                response_message = client_socket.recv(1024).decode()
        else:
            response_message = "Unknown choice."
    
    except Exception as e:
        response_message = f"Error communicating with server: {e}"
    
    return response_message

@app.route('/register', methods=['GET', 'POST'])
def main():
    response_message = ''
    
    if request.method == 'POST':
        user_choice = request.form["user_choice"]
        ftp_choice = request.form.get("ftp_choice", "N")
        ftp_username = request.form.get("ftp_username", "")
        ftp_password = request.form.get("ftp_password", "")
        image_path = request.form.get("image_path", "")
        
        response_message = communicate_with_server(user_choice, ftp_choice, ftp_username, ftp_password, image_path)
        
    return render_template('index.html', response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)
