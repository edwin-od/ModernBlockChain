import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disconn!"

PORT = 3456
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)

def handle_client(conn, addr):
    print(f"[CLIENT CONNECTED] {addr}")

    connected = True
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
                if msg == DISCONNECT_MSG:
                    connected = False
                    break;
                print(f"[{addr}] {msg}")

    conn.close()
    print(f"[CLIENT DISCONNECTED] {addr}")



def start():
    s.listen()
    print(f"[SERVER STARTED] {SERVER}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("----server starting----")
start()