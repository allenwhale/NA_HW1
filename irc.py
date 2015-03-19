import socket
import sys

HOST = 'irc.twitch.tv'
PORT = 6667
NICK = 'allencat850502'
IDNET = 'ALLEN'
REALNAME = 'allenwhale'
KEY = 'oauth:m9cv6y0v8jlusvn1xu4brpc67lbw6w'
if __name__ == '__main__':
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    print('start connecting')
    try:
        s.connect((HOST, PORT))
    except:
        print('socket connection failed')
    s.sendall(str.encode('PASS %s\r\n' % KEY))
    s.sendall(str.encode('NICK %s\r\n' % NICK))
    data = bytes.decode(s.recv(1024))
    sock_buffer = ''
    while True:
        sock_buffer += s.recv(1024)
        print(sock_buffer)

