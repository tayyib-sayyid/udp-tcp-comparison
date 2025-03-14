import socket

def main():
    HOST = '127.0.0.1'
    PORT = 12345        

    # creating a tcp socket bound to address
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"TCP server listening on {HOST}:{PORT}")

    #accept connection
    conn, addr = server_socket.accept()
    print("Connected by", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break 
        message = data.decode()
        print("Received:", message)
        response = "Received: " + message
        conn.sendall(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    main()
