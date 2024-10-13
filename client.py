import socket
import threading

def client_thread(client_id):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 2220))  # Connect to load balancer
    
    message = f"Selamat pagi dari client {client_id}!"
    client.send(message.encode('utf-8'))

    # Receive reply from load balancer
    reply = client.recv(1024).decode('utf-8')
    print(f"Client {client_id} received: {reply}")

    client.close()

def start_clients(num_clients):
    threads = []
    for i in range(num_clients):
        thread = threading.Thread(target=client_thread, args=(i+1,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start_clients(100)  # Start 100 clients
