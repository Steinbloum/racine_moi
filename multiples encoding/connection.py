import socket

HEADER = 64
PORT = 52017
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONECT"
SERVER = "challenge01.root-me.org"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_lenght = len(message)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' *(HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(message)
    

msg = client.recv(2048).decode(FORMAT)
print(msg)
enigma = msg.split(' ')[-2]
print(f"The code to decipher is : {enigma}")
