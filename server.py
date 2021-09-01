import socket
import os
import sys
import select
import thread

from constants import *

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST,PORT))
    server.listen(BACKLOG)
    input = [server]
    dict = {}
    
    while True:
        inready,outready,exceptready = select.select(input, [], [])
        for serv in inready:
            if (serv == server):
                client, addr = server.accept()
                input.append(client)
            else:
                start(serv,input,dict)

def start(client, input, dict):
    try:
        data = client.recv(DATA_SIZE)

        if (data.strip() == '\help'):
            usage(client)
        if (data.strp() == '\GET_CLIENTS'):
            client.send('\CLIENT_LIST: ' + str(dict.keys()))
        if (data.strip() == '\DISCONNECT'):
            client.close()
            input.remove(client)
        else:
            pass
    except:
        client.close()
        input.remove(client)

def usage(client):
    msg = '''
Command List:

\GET_CLIENTS      - request list of connected clients

\DISCONNECT    - disconnect from service '''
    client.send(msg)

def info(client, client_info):
    client.send('username: ')
    user = client.recv(DATA_SIZE)
    if (client_info.has_key(user)):
        client.send(client_info[user])
    else:
        client.send('User ' + user + ' does not exist')

if __name__ == '__main__':
    main()
