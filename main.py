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
    CmdHandlerList = [NormalHandler(ExecuteHandler(KeyboardHandler())), 
    DemocracyHandler(ExecuteHandler(KeyboardHandler()), 5), 
    ViolenceHandler(ExecuteHandler(KeyboardHandler()), 5)]
    irc.run(CmdHandlerList, LogHandler('log'), ParserHandler())
