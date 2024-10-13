import socket
import threading
import logging

# Setup logging to record connection times and messages
logging.basicConfig(filename="server_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

def handle_client(client_socket, address):
    logging.info(f"New connection from {address}")
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            logging.info(f"Message received from {address}: {message}")
            reply = f"Server {address[1]} received: {message}"
            client_socket.send(reply.encode('utf-8'))
            logging.info(f"Reply sent to {address}")

        except ConnectionResetError:
            logging.info(f"Connection with {address} was closed.")
            break

    client_socket.close()
    logging.info(f"Connection closed with {address}")

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", port))
    server.listen(5)
    print(f"[*] Server listening on port {port}")

    while True:
        client_socket, addr = server.accept()
        logging.info(f"Accepted connection from {addr} on port {port}")

        # Start a new thread to handle client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    # Start three servers on different ports
    ports = [2221, 2222, 2223]
    for port in ports:
        thread = threading.Thread(target=start_server, args=(port,))
        thread.start()
