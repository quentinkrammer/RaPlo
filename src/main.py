# -*- coding: utf-8 -*-
'''

'''
import socket

def writeToFile(txt):
    f = open(".\data\testdatenX.txt", "a")
    f.write(txt)
    f.close()

if __name__ == '__main__':
    

    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 1337        # The port used by the server
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        #s.sendall(b'Hello, world')
        while(True):
            data = s.recv(int(4.0E7))
            writeToFile(data.decode())
           
    
    