from irc import twitch_IRC
from log import LogHandler
from myparser import ParserHandler
from normal import NormalHandler
from execute import ExecuteHandler
from democracy import DemocracyHandler
from violence import ViolenceHandler
from reverse import ReverseHandler
from keyboard import KeyboardHandler

if __name__ == '__main__':
    irc = twitch_IRC('allencat850502', 'oauth:xleqdic11ra8bcb76a3chw93ya6t12')
    CmdHandlerList = [NormalHandler(ExecuteHandler(KeyboardHandler())), 
    DemocracyHandler(ExecuteHandler(KeyboardHandler()), 3), 
    ViolenceHandler(ExecuteHandler(KeyboardHandler()), 3),
    ReverseHandler(ExecuteHandler(KeyboardHandler()))]
    irc.run(CmdHandlerList, LogHandler('log'), ParserHandler())
