import socket 
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

attacker_ip = ''

listener = socket.socket(AF_INET, SOCK_STREAM)
listener.setsockopt(SOL_SOCKET, SO_REUSEADDR)
listener.bind((attacker_ip, 4444))

listener.listen(0)
listener.accept()