from irc import twitch_IRC
from log import LogHandler
from parser import ParserHandler
from normal import NormalHandler
from execute import ExecuteHandler
from democracy import DemocracyHandler
from violence import ViolenceHandler

if __name__ == '__main__':
    irc = twitch_IRC('allencat850502', 'oauth:m9cv6y0v8jlusvn1xu4brpc67lbw6w')
    irc.run(ViolenceHandler(ExecuteHandler(), 5), LogHandler('log'), ParserHandler())
