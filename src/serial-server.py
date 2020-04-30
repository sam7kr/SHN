#! /usr/bin/python3.7

import argparse, socket, serial


def server(interface, sp, port):
    ser = serial.Serial(sp, 9600, timeout=1)
    global message
    message = ""
    while message != "burn": # for keeping the server listening
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((interface, port))
        sock.listen(1)
        print('Listening at', sock.getsockname())
        cl, sockname = sock.accept()
        print('Accepted connection from', sockname)
        while True:
            try:
                message = cl.recv(255)
                ser.write(message)
                fromArduino = ser.read(255)
                message = message.decode('ascii')
                print(' Incoming message:', message)
                cl.sendall(fromArduino.encode('ascii'))
                if message == "kill" or message == "burn":
                    cl.sendall("kill".encode('ascii'))
                    cl.close()
                    break
            except ConnectionAbortedError:
                break
        print('Server Closed')
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('host', help='server interface')
    parser.add_argument('sp', metavar='PORT', help='Serial port')
    parser.add_argument('-p', metavar='PORT', type=int, default=55777, help='TCP port (default 55777)')
    args = parser.parse_args()
    server(args.host, args.sp, args.p)













