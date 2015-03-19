from irc import twitch_IRC
from log import LogHandler

if __name__ == '__main__':
    irc = twitch_IRC('allencat850502', 'oauth:m9cv6y0v8jlusvn1xu4brpc67lbw6w')
    irc.run(None, LogHandler('log'))
