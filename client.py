import socket
#import pickle ==> used to send objects that are not strings


HEADER = 64 # way too large
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = #add server ip
ADDR = (SERVER, PORT)

#test connection by going to cmd and type in (while in correct folder) python client.py

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT) #always encode messages into bites before sending
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))   #make the message HEADER length
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT)) #concerning 2048: ideally use same protocal to receive as to send
    
send("Hello World")
input()
send("Hello Everyone")
input()
send("Hello me!")
input()
send(DISCONNECT_MESSAGE)

