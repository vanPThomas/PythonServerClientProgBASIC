import socket
import threading

HEADER = 64 #way too large
PORT = 5050                         
SERVER = socket.gethostbyname(socket.gethostname())     #type ipconfig  in command prompt to know IP adress
ADDR = (SERVER, PORT) #tupple
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#print(SERVER)
#print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:  #check if there is an actual message
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Message Received".encode(FORMAT))
    conn.close()    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:                         #continue to listen
        conn, addr = server.accept()    #waits for connection, stores adress and object in conn
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")
        
print("[STARTING] server is starting ...")
start()

#over the internet: look up public ip adress
# change SERVER to that ip