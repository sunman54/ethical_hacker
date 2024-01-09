import socket 

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('192.168.106.129',4444))

connection.send('\n[+] Connected!!!\n')

recieved_data = connection.recv(1024)
pribt(recieved_data)

connection.close()