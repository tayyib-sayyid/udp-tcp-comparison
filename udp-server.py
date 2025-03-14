import socket
import random

def main():
    HOST = '127.0.0.1'  
    PORT = 12346        #port diff from tcp

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    print(f"UDP server listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)
        if not data:
            continue
        message = data.decode()
        print(f"Received from {addr}: {message}")

        if random.random() < 0.2:
            print("Simulated packet loss for message:", message)
            continue

        response = "Received: " + message
        server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    main()
