import socket
import os
import sys
import select
import _thread

from constants import *

class Server:
    connections = []
    peers = []

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((HOST, PORT))
        sock.listen(self, BACKLOG)
        print("Server running...")

        while True:
            cSocket, cAddr = sock.accept()
            cThread = threading.Thread(target = self.handler, args=(cSocket, cAddr))
            cThread.daemon = True
            cThread.start()
            self.connection.append(cSocket)
            self.peers.append(cAddr[0])
            self.sendPeers()
            print(cAddr[0] + ":" + cAddr[1] + " Connected!")

    def handler(self, cSocket, cAddr):
        while True:
            data = cSocket.recv(DATA_SIZE)

            for connect in self.conncetions:
                if connect != cSocket:
                    connect.send(bytes(data, "utf-8"))
            if not data:
                print(cAddr[0] + ":" + cAddr[1] + " Disconnected!")
                self.connection.remove(cSocket)
                self.peers.remove(cAddr[0])
                cSocket.close()
                self.sendPeers()
                break

    def sendPeers(self):
        p = ""
        for peer in self.peers:
            p = p + peer + ","
        for connect in self.connection:
            connect.send(b'\x11' + bytes(p, "utf-8"))

#
# def main():
#
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#
#     server.bind((HOST,PORT))
#     server.listen(BACKLOG)
#     input = [server]
#     dict = {}
#
#     while True:
#         read_sockets,write_sockets,error_sockets = select.select(input, [], [])
#         for sock in read_sockets:
#             if (sock == server):
#                 client, addr = server.accept()
#                 input.append(client)
#             else:
#                 start(sock,input,dict)
#                 print("Client connected")
#
# def listen(client):
#     client.send('Enter port to listen on: ')
#     client_port = client.recv(DATA_SIZE)
#
#
# def start(client, input, dict):
#     try:
#         data = client.recv(DATA_SIZE)
#         client.send('Type request: ')
#         if (data.strip() == '\LISTEN'):
#             listen(client)
#         if (data.strip() == '\help'):
#             usage(client)
#         if (data.strip() == '\DISCONNECT'):
#             client.close()
#             input.remove(client)
#         else:
#             pass
#     except:
#         client.close()
#         input.remove(client)
#
# def usage(client):
#     msg = '''
# Command List:
#
# \DISCONNECT    - disconnect from service '''
#     client.send(msg)
#
# if __name__ == '__main__':
#     main()
