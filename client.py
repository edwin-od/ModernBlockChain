import socket

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disconn!"

PORT = 3456
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

def send(message):
    msg = message.encode(FORMAT) + b' ' * (HEADER - len(message.encode(FORMAT)))
    s.send(msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)

send("Hello World")

send(DISCONNECT_MSG)