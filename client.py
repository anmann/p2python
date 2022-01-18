
import socket
import os
import sys
import select
import _thread
import threading

from constants import *

class Client:

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((HOST,PORT))
        cThread = threading.Thread(target = self.sendMsg, args=(sock, ))
        cThread.daemon = True
        cThread.start()
        print("Server: " + " Connected as Client.")

        while True:
            data = sock.recv(DATA_SIZE)
            if not data:
                break
            else:
                print((str(data, "utf-8")))

    def peersUpdated(self, peerData):
        p2python.peers = str(peerData, "utf-8").split(",")[:1]

    def sendMsg(self, sock):
        while True:
            sock.send(bytes(input(""),"utf-8"))
