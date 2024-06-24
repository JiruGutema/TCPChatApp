import socket
import time
import os
import platform
import threading

class Client:
    """
    A TCP client that can connect to a server, send messages, and receive messages.
    """

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_ip = None
        self.server_port = 12345
        self.connection_established = False

    def connect_to_server(self):
        """
        Establish a connection with the server.
        """
        while not self.connection_established:
            try:
                self.server_ip = input("Enter server IP address (e.g., 127.0.0.1): ")
                server = (self.server_ip, self.server_port)
                self.client_socket.connect(server)
                self.connection_established = True
                print("Connection successful.")
            except socket.error as e:
                print(f"Error connecting to server: {e}")
                print("Retrying connection...")
                time.sleep(1)
                if platform.system().lower().startswith('win'):
                    os.system('cls')
                else:
                    os.system('clear')

    def send_message(self, message):
        """
        Send a message to the connected server.
        """
        self.client_socket.send(message.encode())

    def receive_messages(self):
        """
        Receive messages from the connected server and print them.
        """
        while True:
            try:
                data = self.client_socket.recv(1024).decode()
                if data:
                    print(data)
                else:
                    break
            except socket.error as e:
                print(f"Error receiving message: {e}")
                break

    def chat_room(self):
        """
        Manage the chat room functionality.
        """
        self.connect_to_server()
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        while True:
            message = input("Enter your message (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            message = f"\nClient: {message}"
            self.send_message(message)

if __name__ == '__main__':
    client = Client()
    client.chat_room()