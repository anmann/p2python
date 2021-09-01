
import socket
import os
import sys
import select
import thread

HOST = '127.0.0.1'
PORT = 8888
BACKLOG = 10
DATA_SIZE = 2048
TEMP = 0

