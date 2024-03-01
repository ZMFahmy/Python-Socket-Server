import socket

# Define the host and port to connect to
HOST, PORT = "localhost", 9999

# Define a list of test cases
test_cases = [
    "Wpython Socket Server",
    "LpythonSocketServer",
    "UPYTHONSOCKETSERVER",
    "R1234567890",
    "TpythonSocketServer123",
    "pythonSocketServer123",
]

# Iterate over each test case
for case in test_cases:
    data = case

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to the server
        sock.connect((HOST, PORT))

        # Send the test case data to the server
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server
        received = str(sock.recv(1024), "utf-8")

    # Print the input data and received output
    print("Input:  {}".format(data))
    print("Output: {}".format(received) + "\n")
