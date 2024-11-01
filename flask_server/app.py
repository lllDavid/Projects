from flask import Flask, render_template, request
import socket
import time

app = Flask(__name__)

def send_to_socket_server(command):
    server_address = ('127.0.0.1', 1234)  # Replace with your server's address and port
    max_attempts = 5
    attempt = 0

    while attempt < max_attempts:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(server_address)
                s.sendall(command.encode('utf-8'))
                response = s.recv(1024)
                return response.decode('utf-8')
        except Exception as e:
            attempt += 1
            time.sleep(1)

    return "Failed to communicate with the server after multiple attempts."

@app.route('/register', methods=['GET', 'POST'])
def register():
    response_message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        command = f"REGISTER {username} {password}"  # Format your command as needed
        response_message = send_to_socket_server(command)

    return render_template('register.html', response_message=response_message)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
