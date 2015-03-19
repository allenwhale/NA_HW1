import socket
import sys
import time

HOST = 'irc.twitch.tv'
PORT = 6667
NICK = 'allencat850502'
IDENT = 'ALLEN'
REALNAME = 'allenwhale'
KEY = 'oauth:m9cv6y0v8jlusvn1xu4brpc67lbw6w'
CHANNEL = '#allencat850502'
if __name__ == '__main__':
    s=socket.socket()
    #s.settimeout(5)
    print('start connecting')
    try:
        s.connect((HOST, PORT))
    except:
        print('socket connection failed')
    s.send(('PASS %s\r\n' % KEY).encode())
    s.send(('NICK %s\r\n' % NICK).encode())
    s.send(("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME)).encode())
    s.send(('JOIN %s\r\n' % CHANNEL).encode())
    sock_buffer = ''
    while True:
        sock_buffer  += s.recv(1024).decode()
        print(sock_buffer)
        if sock_buffer.find('PING') != -1:
            s.send(('PONG %s\r\n' % sock_buffer.split('PING')[1]).encode())

