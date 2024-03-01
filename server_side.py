import socketserver


# Define a custom TCP server class inheriting from TCPServer
class MyTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, request_handler):
        super().__init__(server_address, request_handler)


# Define a custom request handler class inheriting from BaseRequestHandler
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    # Handle method for processing incoming client requests
    def handle(self):
        # self.request is the TCP socket connected to the client
        # Receive data from the client
        self.data_encoded = self.request.recv(1024).strip()
        self.data_decoded = self.data_encoded.decode("utf-8")

        # Print the received data and client's IP address
        print(f"Received from {self.client_address[0]}:   {self.data_encoded}")

        # Extract operation type and input message from received data
        operation_type = self.data_decoded[0]
        input_message = self.data_decoded[1:]

        # Perform the operation based on the operation type
        if operation_type == 'W':
            word_count = 0
            for char in input_message:
                if char == ' ':
                    word_count += 1
            output = f"The number of words is {word_count + 1}"
        elif operation_type == 'L':
            lowercase_count = 0
            for char in input_message:
                if char.islower():
                    lowercase_count += 1
            output = f"The number of lowercase letters is {lowercase_count}"
        elif operation_type == 'U':
            uppercase_count = 0
            for char in input_message:
                if char.isupper():
                    uppercase_count += 1
            output = f"The number of uppercase letters is {uppercase_count}"
        elif operation_type == 'R':
            numeric_count = 0
            for char in input_message:
                if char.isdigit():
                    numeric_count += 1
            output = f"The number of numeric characters is {numeric_count}"
        elif operation_type == 'T':
            char_count = 0
            for char in input_message:
                char_count += 1
            output = f"The total number of characters is {char_count}"
        else:
            output = self.data_decoded

        # Send the result back to the client
        self.request.sendall(output.encode("utf-8"))


# Define the host and port for the server
HOST, PORT = "localhost", 9999

# Create an instance of the custom TCP server
server = MyTCPServer((HOST, PORT), MyTCPHandler)

try:
    # Start the server and listen for incoming connections
    server.serve_forever()
except KeyboardInterrupt:
    # Shutdown the server gracefully on keyboard interrupt
    server.shutdown()
    server.server_close()
    print("Server has shutdown successfully")
