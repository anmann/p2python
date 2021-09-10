import socket
import os
import sys
import select
import _thread

from constants import *

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST,PORT))
    server.listen(BACKLOG)
    input = [server]
    dict = {}
    
    while True:
        read_sockets,write_sockets,error_sockets = select.select(input, [], [])
        for sock in read_sockets:
            if (sock == server):
                client, addr = server.accept()
                input.append(client)
            else:
                start(sock,input,dict)

def start(client, input, dict):
    #try:
    data = client.recv(DATA_SIZE)

    if (data.strip() == '\help'):
        usage(client)
    if (data.strip() == '\DISCONNECT'):
        client.close()
        input.remove(client)
    else:
        pass
    #except:
     #   client.close()
      #  input.remove(client)

def usage(client):
    msg = '''
Command List:

\DISCONNECT    - disconnect from service '''
    client.send(msg)

if __name__ == '__main__':
    main()
