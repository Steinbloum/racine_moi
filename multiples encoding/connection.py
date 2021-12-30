import socket
import time
from mulenc import d

HEADER = 64
PORT = 52017
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONECT"
SERVER = "challenge01.root-me.org"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

def send(msg):
    message = msg.encode(FORMAT)
    # msg_lenght = len(message)
    # send_lenght = str(msg_lenght).encode(FORMAT)
    # send_lenght += b' ' *(HEADER - len(send_lenght))
    # client.send(send_lenght)
    client.send(message)
    # print(client.recv(2048).decode(FORMAT))
    


while True:
    msg = client.recv(2048).decode(FORMAT)
    print(msg)
    answer = d.run_decypher(msg)
    print(f'The answer is {answer}')
    send(f'{answer}\n')
    # enigma = msg.split(' ')[-2]
    # # print(enigma)
    # enigma = enigma.split('\n')[0]
    # # print(enigma)
    # enigma = enigma.strip("'")
    # # print(enigma)
    # # print(f'The message to decypher is {enigma}')

    # send(f'{answer.lower()}\n')

# print(f"The code to decipher is : {enigma}")
# print(client.recv(2048).decode(FORMAT))
    