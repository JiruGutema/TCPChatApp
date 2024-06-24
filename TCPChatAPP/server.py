import socket
import threading
import time

class Server:
    def __init__(self):
        # Create a TCP socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set the host and port
        self.host = "localhost"
        self.port = 12345
        
        # Bind the socket to the host and port
        server_config = (self.host, self.port)
        self.server.bind(server_config)
        
        # Listen for incoming connections
        self.server.listen(5)
        
        # Accept a connection from a client
        self.clientsocket, self.addr = self.server.accept()
        print("Received connection from", self.addr)
    
    def receive_messages(self):
        """Receive messages from the client"""
        try:
            while True:
                data = self.clientsocket.recv(1024).decode()
                time.sleep(0.001)
                print("Client:", data)
        except Exception as ex:
            print("An error occurred:", ex)
    
    def send_messages(self):
        """Send messages to the client"""
        while True:
            server_message = input("Server: ")
            server_message = f"\nServer: {server_message}\n"
            self.clientsocket.send(server_message.encode())
    
    def run(self):
        """Start the server and handle client communication"""
        # Start a separate thread to receive messages from the client
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()
        
        # Handle sending messages to the client
        self.send_messages()
        
        # Wait for the receive thread to finish
        receive_thread.join()
        
        # Close the server socket
        self.server.close()

if __name__ == '__main__':
    server = Server()
    server.run()