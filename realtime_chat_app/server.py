import socket, threading

def handle_client(conn, addr):
    print(f"Connected: {addr}")
    while True:
        msg = conn.recv(1024)
        if not msg: break
        print(f"{addr}: {msg.decode()}")
        conn.sendall(msg)

def main():
    s = socket.socket()
    s.bind(("0.0.0.0", 5000))
    s.listen()
    print("Chat server running...")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
