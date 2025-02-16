from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_server(host='0.0.0.0', port=21):
    authorizer = DummyAuthorizer()

    authorizer.add_user('test', '123', 'D:\\FTP', perm='elradfmwMT') 

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((host, port), handler)

    server.serve_forever()

start_server()
