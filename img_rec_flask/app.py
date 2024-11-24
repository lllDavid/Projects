from flask import Flask, render_template, request, session, redirect
import socket

app = Flask(__name__)

host = "127.0.0.1"
port = 1234

# Set a secret key for session management (needed for sessions)
app.secret_key = 'your_secret_key'

# Helper function to handle socket communication
def communicate_with_server(user_choice, ftp_choice, ftp_username=None, ftp_password=None, image_path=None):
    response_message = ''
    
    try:
        # If there's already a socket in the session, reuse it
        if 'client_socket' in session:
            client_socket = session['client_socket']
        else:
            # Create a new socket if not available
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

            # Store only necessary connection info in session, not the socket itself
            session['client_socket_connected'] = True  # Store a flag that connection is established
            
        print("Successfully connected to the server.")
        
        # Send user choice
        client_socket.sendall(user_choice.encode())
        
        if user_choice == "3":  # Image recognition option
            client_socket.sendall(ftp_choice.encode())  # Send FTP choice
            
            if ftp_choice == "Y":  # If FTP upload is chosen
                client_socket.sendall(ftp_username.encode())  # Send FTP username
                client_socket.sendall(ftp_password.encode())  # Send FTP password

                # Wait for server to prompt for file upload path
                response_message = client_socket.recv(1024).decode()

                if response_message == "Please send the file path to upload:":
                    client_socket.sendall(image_path.encode())
                    response_message = client_socket.recv(1024).decode()  # Get the result from server
            elif ftp_choice == "N":  # Direct image path
                client_socket.sendall(image_path.encode())  # Send image path for recognition
                response_message = client_socket.recv(1024).decode()  # Get result from server
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
        ftp_choice = request.form.get("ftp_choice", "N")  # Default to "N" if not provided
        ftp_username = request.form.get("ftp_username", "")
        ftp_password = request.form.get("ftp_password", "")
        image_path = request.form.get("image_path", "")
        
        # Call the function to communicate with the server
        response_message = communicate_with_server(user_choice, ftp_choice, ftp_username, ftp_password, image_path)
        
    return render_template('index.html', response_message=response_message)

if __name__ == '__main__':
    app.run(debug=True)
