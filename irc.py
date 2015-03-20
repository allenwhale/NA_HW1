import socket
import sys
import re
import datetime


class twitch_IRC:
    def __init__(self, username, key, buffer_size=2048):
        self.HOST = 'irc.twitch.tv'
        self.PORT = 6667
        self.USER = username
        self.NICK = username
        self.IDENT = username
        self.REALNAME = username
        self.CHANNEL = '#' + username
        self.KEY = key
        self.BUFFER_SIZE = buffer_size
        err = self.connect()
        if err:
            print(err)
            exit(1)
        print('SUCCESSFULLY CONNECTED')

    def recv(self):
        return self.s.recv(self.BUFFER_SIZE).decode()

    def send(self, m):
        self.s.send(m.encode())


    def connect(self):
        print('START CONNECTING')
        self.s = socket.socket()
        try:
            self.s.connect((self.HOST, self.PORT))
        except:
            print('CONNECTION ERROR')
            return 'Econnect'
        print('OAUTH')
        self.s.send(('PASS %s\r\n' % self.KEY).encode())
        self.s.send(('NICK %s\r\n' % self.NICK).encode())
        self.s.send(("USER %s %s bla :%s\r\n" % (self.IDENT, self.HOST, self.REALNAME)).encode())
        self.s.send(('JOIN %s\r\n' % self.CHANNEL).encode())
        tmp = self.recv()
        if tmp == ':tmi.twitch.tv NOTICE * :Login unsuccessful\r\n':
            return 'EAuth'
        print('OAUTH pass')
        return None

    def convert(self, m):
        m = m.split('\r\n')
        ret = []
        for line in m:
            if line.find('PING') != -1:
                self.send('PONG %s\r\n' % line.split()[1])
            else:
                if line.find('PRIVMSG') != -1:
                    r = re.search(':(.*)!(.*)@(.*)\sPRIVMSG #(.*)\s:(.*)', line)
                    ret.append({'user': r.group(1),
                        'time': datetime.datetime.now(),
                        'message': r.group(5)})
        return ret

    def run(self, CmdHandler, LogHandler, ParserHandler):
        while True:
            message = self.recv()
            message = self.convert(message)     
            LogHandler.log(message)
            for m in message:
                m['cmd'] = ParserHandler.parser(m['message'])
			print(message)
            CmdHandler.execute(message)
            print(message)

