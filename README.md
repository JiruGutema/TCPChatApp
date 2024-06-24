Here's the README.md file for both the client and server scripts:

# Commandline Chat Application in Python

This repository contains a simple commandline chat application built using sockets in Python. It consists of a server script and a client script.

## Getting Started

1. Clone the repository:

```
git clone https://github.com/JiruGutema/TCPChatApp.git
cd TCPChatApp.git
```

2. Run the server script:

```
python server.py
```

3. Run the client script:

```
python client.py
```

The client will be prompted to enter the server's IP address. Once the connection is established, you can start chatting.

## How it Works

The `Server` class in `server.py` sets up a TCP socket, binds it to a host and port, and listens for incoming connections. When a client connects, the server accepts the connection and starts two separate threads:

1. `receive_messages()`: This thread receives messages from the client and prints them.
2. `send_messages()`: This thread allows the server to send messages to the client.

The `Client` class in `client.py` sets up a TCP socket and connects to the server. It also starts two separate threads:

1. `connect_to_server()`: This thread attempts to connect to the server and retries if the connection fails.
2. `receive_messages()`: This thread receives messages from the server and prints them.

The `chat_room()` method in the `Client` class manages the chat room functionality, allowing the user to send and receive messages.

## Usage

1. Start the server script:
   ```
   python server.py
   ```
2. Start the client script:
   ```
   python client.py
   ```
3. Enter the server's IP address when prompted.
4. Start chatting! Type your message and press Enter to send it.
5. To exit the chat, type "exit" and press Enter.

## Dependencies

- Python 3.x

## Contributing

If you find any issues or have ideas for improvements, feel free to open an issue or submit a pull request.
