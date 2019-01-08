import socket
import time
import sys

server_IP = '192.168.88.1'
server_port = 8888
server_addr = (server_IP , server_port)

socket_tcp = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

def Connect_the_pi():
    while True: # try to connect the server
        try:
            print('Connecting the pi: 192.168.88.1:8888')
            socket_tcp.connect(server_addr)
            print('Done\n' + 'Initializing the window. Welcome!')
            break
        except Exception:
            time.sleep(1)
            continue

def Send_message(to_send):
    while True:
        try:
            socket_tcp.send(to_send.encode())
            break
        except Exception:
            time.sleep(0.5)
            print('trying again')
            continue

def Exit_connection(socket_tcp):
    socket_tcp.close()
    socket_tcp = None
    print('Connection Terminated. Bye!')
    sys.exit(1)