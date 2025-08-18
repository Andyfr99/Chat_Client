import socket
import threading
from time import sleep as wait

client = None

def close():
    global client
    client.close()

def recieve_message():
    global client
    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break
            print("\n" + data)
        except:
            break
        
def Main():
    global client
    
    print("Welcome to chat!")

    NAME = str(input("Input your username: "))
    HOST = str(input("HOST to connect to? "))
    PORT = int(input("PORT to connect to? "))
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
    except:
        print(f"no connection found at {HOST}:{PORT}")
        print("(this window will close in 5 seconds)")
        wait(5.0)
        quit()

    print(f"Successfully connected to {HOST}:{PORT}")
    print("type '/quit' to exit the chatroom")

    tread=threading.Thread(target=recieve_message, daemon=True)
    tread.start()

    while True:
        msg = str(input())
        if msg.lower() == "/quit":
            client.sendall(msg.encode())
            break
        elif msg == "":
            pass
        else:
            msg_to_send = (f"{NAME}: {msg}")
            client.sendall(msg_to_send.encode())
            
    print("QUIT")        
    close()
    quit()

if __name__ == '__main__':
    Main()