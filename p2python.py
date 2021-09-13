from client import Client
from server import Server
import time
import sys

peers = ["127.0.0.1"]

def main():
    while True:
        try:
            print("trying to connect...")
            time.sleep(3)
            for peer in peers:
                try:
                    client = Client()
                except:
                    pass
                try:
                    server = Server()
                except:
                    print("exiting...")
        except:
            sys.exit(0)

if __name__ == "__main__":
    main()
