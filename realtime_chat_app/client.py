import socket, threading

def listen(sock):
    while True:
        data = sock.recv(1024)
        if data:
            print("Server:", data.decode())

s = socket.socket()
s.connect(("127.0.0.1", 5000))

threading.Thread(target=listen, args=(s,), daemon=True).start()

while True:
    msg = input()
    s.send(msg.encode())
