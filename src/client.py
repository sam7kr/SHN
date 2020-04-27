#! /usr/bin/python3.7

import argparse, socket

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client connected')
    message = input('S-command: ')
    sock.sendall(message.encode('ascii'))
    replay = sock.recv(4)
    replay = replay.decode('ascii')
    print(replay)
    if replay == "kill":
        sock.close()
        sock = None
    print('Client Closed')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' Send and receive over TCP')
    parser.add_argument('host', help='Server ip')
    parser.add_argument('-p', metavar='PORT', type=int, default=55777, help='Server Port')
    args = parser.parse_args()
    client(args.host, args.p)
        
