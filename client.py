
import socket
import os
import sys
import select

from constants import *

def recvf():


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)

        client.connect((HOST,PORT))

        while True:
            data = client.recv(DATA_SIZE)

    except:
        print("Error, exiting")
        sys.exit()


if __name__ == '__main__':
    main()
