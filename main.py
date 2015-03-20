from irc import twitch_IRC
from log import LogHandler
from myparser import ParserHandler
from normal import NormalHandler
from execute import ExecuteHandler
from democracy import DemocracyHandler
from violence import ViolenceHandler
from keyboard import KeyboardHandler

if __name__ == '__main__':
    irc = twitch_IRC('allencat850502', 'oauth:m9cv6y0v8jlusvn1xu4brpc67lbw6w')
    irc.run(NormalHandler(ExecuteHandler(KeyboardHandler())), LogHandler('log'), ParserHandler())
