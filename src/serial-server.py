#! /usr/bin/python3.7

import argparse, socket, serial



def server(interface, sp, port):
    while message != "burn":
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ser = serial.Serial(sp, 9600, timeout=1)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((interface, port))
        sock.listen(1)
        print('Listening at', sock.getsockname())
        cl, sockname = sock.accept()
        print('Accepted connection from', sockname)
        while True:
            message = cl.recv(1023)
            ser.write(message)
            message = message.decode('ascii')
            print(' Incoming message:', message)
            cl.sendall("done".encode('ascii'))
            if message == "kill":
                cl.sendall("kill".encode('ascii'))
                cl.close()
                break
        print('Server Closed')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('host', help='server interface')
    parser.add_argument('sp', metavar='PORT', help='Serial port')
    parser.add_argument('-p', metavar='PORT', type=int, default=55777, help='TCP port (default 55777)')
    args = parser.parse_args()
    server(args.host, args.sp, args.p)













