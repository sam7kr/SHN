#! /usr/bin/python3.7

import argparse, socket, sys

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('connected')
    message = ""
    while True:
        if message != "kill":
            message = input()
        sock.sendall(message.encode('ascii'))
        response = sock.recv(1023)
        response = response.decode('ascii')
        print(response)

        if response == "kill":
            sock.close()
            break
    print('disconnected')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' Send and receive over TCP')
    parser.add_argument('host', help='Server ip')
    parser.add_argument('-p', metavar='PORT', type=int, default=55777, help='Server Port')
    args = parser.parse_args()
    client(args.host, args.p)

sys.stdout.flush()
