
import socket
import os
import sys
import select

from constants import *

def recvFile(socket):
    data = socket.recv(DATA_SIZE)
    user_raw_input = input(data)
    # currently just working with text files
    file = open('test.txt', 'w')
    file.write(str(data))
    file.close()

def sendFile(socket):
    socket.send("file name: ")
    file_name = socket.recv(DATA_SIZE)
    file = open(file_name, 'rb')
    file_content = file.read()
    socket.send(file_content)

def listen(user_input):
    client_port = int(user_input)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, client_port))

    socket.listen(BACKLOG)

    while True:
        socket_list = [sys.stdin, sock]
        read_sockets,write_sockets,error_sockets = select.select(socket_list, [], [])
        for s in read_sockets:
            try:
                if s == sock:
                    client, address = sock.accept()
                    print("Connected")
                    client.send("Connected: ")
                else:
                    data = s.recv(DATA_SIZE)
                    if data:
                        if data == '\SEND_FILE':
                            sendFile(client)
                        elif data == '\EXIT':
                            client.close()
                            break
            except:
                client.close()
                input.remove(client)

def connect(data):
    client_port = int(data)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        sock.connect((HOST, client_port))
        while True:
            data = sock.recv(DATA_SIZE)

            if data == '\SEND_FILE':
                sendFile(sock)
            elif data == '\EXIT':
                sock.close()
                break
    except:
        sock.close()
        print("Unable to connect")

def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        client.connect((HOST,PORT))

        while True:
            data = client.recv(DATA_SIZE)     
            connect(data)

            user_raw_input = input(data)
            client.send(user_raw_input)
            listen(user_raw_input)
            if user_raw_input == '\DISCONNECT':
                client.close()
                break

    except:
        print("Error, exiting")
        sys.exit()

if __name__ == '__main__':
    main()
