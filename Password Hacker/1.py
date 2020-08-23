import sys
import socket
args = sys.argv

with socket.socket() as client_socket:
    ip_address, port, msg = args[1:]
    client_socket.connect((ip_address, int(port)))
    msg = msg.encode()
    client_socket.send(msg)
    response = client_socket.recv(1024)
    print(response.decode())

