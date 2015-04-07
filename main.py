from irc import twitch_IRC
from log import LogHandler
from myparser import ParserHandler
from normal import NormalHandler
from execute import ExecuteHandler
from democracy import DemocracyHandler
from violence import ViolenceHandler
from keyboard import KeyboardHandler

if __name__ == '__main__':
    irc = twitch_IRC('allencat850502', 'oauth:x69xegnjzqg3c41269w2r4mmbdm1w9')
    CmdHandlerList = [NormalHandler(ExecuteHandler(KeyboardHandler())), 
    DemocracyHandler(ExecuteHandler(KeyboardHandler()), 5), 
    ViolenceHandler(ExecuteHandler(KeyboardHandler()), 5)]
    irc.run(CmdHandlerList, LogHandler('log'), ParserHandler())
