# Generated from MissionControl.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,144,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,5,1,33,8,1,10,1,12,1,36,9,1,1,1,1,1,1,1,1,2,1,2,1,2,
        5,2,44,8,2,10,2,12,2,47,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,55,8,3,1,
        4,1,4,1,4,5,4,60,8,4,10,4,12,4,63,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,3,5,74,8,5,1,5,3,5,77,8,5,1,6,1,6,1,6,5,6,82,8,6,10,6,
        12,6,85,9,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,93,8,7,10,7,12,7,96,9,7,
        1,7,1,7,1,8,1,8,1,8,5,8,103,8,8,10,8,12,8,106,9,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,124,8,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,135,8,9,1,10,1,10,1,10,1,10,
        1,10,3,10,142,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,
        0,21,22,148,0,22,1,0,0,0,2,25,1,0,0,0,4,40,1,0,0,0,6,50,1,0,0,0,
        8,56,1,0,0,0,10,66,1,0,0,0,12,78,1,0,0,0,14,88,1,0,0,0,16,99,1,0,
        0,0,18,134,1,0,0,0,20,136,1,0,0,0,22,23,3,2,1,0,23,24,5,0,0,1,24,
        1,1,0,0,0,25,26,5,7,0,0,26,27,5,20,0,0,27,28,5,13,0,0,28,29,3,4,
        2,0,29,30,3,8,4,0,30,34,3,12,6,0,31,33,3,14,7,0,32,31,1,0,0,0,33,
        36,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,34,1,0,0,
        0,37,38,3,16,8,0,38,39,5,14,0,0,39,3,1,0,0,0,40,41,5,8,0,0,41,45,
        5,13,0,0,42,44,3,6,3,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,
        45,46,1,0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,14,0,0,49,5,1,
        0,0,0,50,51,5,19,0,0,51,52,5,17,0,0,52,54,7,0,0,0,53,55,5,18,0,0,
        54,53,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,0,56,57,5,9,0,0,57,61,5,13,
        0,0,58,60,3,10,5,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,
        62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,14,0,0,65,9,1,0,0,
        0,66,67,5,20,0,0,67,68,5,17,0,0,68,69,5,21,0,0,69,70,5,18,0,0,70,
        73,5,21,0,0,71,72,5,18,0,0,72,74,5,21,0,0,73,71,1,0,0,0,73,74,1,
        0,0,0,74,76,1,0,0,0,75,77,5,18,0,0,76,75,1,0,0,0,76,77,1,0,0,0,77,
        11,1,0,0,0,78,79,5,10,0,0,79,83,5,13,0,0,80,82,3,18,9,0,81,80,1,
        0,0,0,82,85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,
        83,1,0,0,0,86,87,5,14,0,0,87,13,1,0,0,0,88,89,5,11,0,0,89,90,5,20,
        0,0,90,94,5,13,0,0,91,93,3,18,9,0,92,91,1,0,0,0,93,96,1,0,0,0,94,
        92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,14,
        0,0,98,15,1,0,0,0,99,100,5,12,0,0,100,104,5,13,0,0,101,103,3,18,
        9,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,
        0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,108,5,14,0,0,108,17,1,0,
        0,0,109,110,5,1,0,0,110,111,5,15,0,0,111,112,7,0,0,0,112,135,5,16,
        0,0,113,114,5,2,0,0,114,115,5,15,0,0,115,135,5,16,0,0,116,117,5,
        3,0,0,117,118,5,15,0,0,118,135,5,16,0,0,119,120,5,4,0,0,120,123,
        5,15,0,0,121,124,5,20,0,0,122,124,3,20,10,0,123,121,1,0,0,0,123,
        122,1,0,0,0,124,125,1,0,0,0,125,135,5,16,0,0,126,127,5,5,0,0,127,
        128,5,15,0,0,128,129,7,0,0,0,129,135,5,16,0,0,130,131,5,6,0,0,131,
        132,5,15,0,0,132,133,7,0,0,0,133,135,5,16,0,0,134,109,1,0,0,0,134,
        113,1,0,0,0,134,116,1,0,0,0,134,119,1,0,0,0,134,126,1,0,0,0,134,
        130,1,0,0,0,135,19,1,0,0,0,136,137,5,21,0,0,137,138,5,18,0,0,138,
        141,5,21,0,0,139,140,5,18,0,0,140,142,5,21,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,21,1,0,0,0,12,34,45,54,61,73,76,83,94,104,123,134,
        141
    ]

class MissionControlParser ( Parser ):

    grammarFileName = "MissionControl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'takeoff'", "'land'", "'rtl'", "'goto'", 
                     "'hover'", "'speed'", "'mission'", "'settings'", "'waypoints'", 
                     "'start'", "'task'", "'end'", "'{'", "'}'", "'('", 
                     "')'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MISSION", 
                      "SETTINGS", "WAYPOINTS", "START", "TASK", "END", "LBRACE", 
                      "RBRACE", "LPAREN", "RPAREN", "COLON", "COMMA", "ID", 
                      "STRING", "FLOAT", "NUMBER", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_missionBlock = 1
    RULE_settingsBlock = 2
    RULE_settingsEntry = 3
    RULE_waypointsBlock = 4
    RULE_waypointEntry = 5
    RULE_startBlock = 6
    RULE_taskBlock = 7
    RULE_endBlock = 8
    RULE_command = 9
    RULE_geoCoords = 10

    ruleNames =  [ "prog", "missionBlock", "settingsBlock", "settingsEntry", 
                   "waypointsBlock", "waypointEntry", "startBlock", "taskBlock", 
                   "endBlock", "command", "geoCoords" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    MISSION=7
    SETTINGS=8
    WAYPOINTS=9
    START=10
    TASK=11
    END=12
    LBRACE=13
    RBRACE=14
    LPAREN=15
    RPAREN=16
    COLON=17
    COMMA=18
    ID=19
    STRING=20
    FLOAT=21
    NUMBER=22
    COMMENT=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def missionBlock(self):
            return self.getTypedRuleContext(MissionControlParser.MissionBlockContext,0)


        def EOF(self):
            return self.getToken(MissionControlParser.EOF, 0)

        def getRuleIndex(self):
            return MissionControlParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = MissionControlParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.missionBlock()
            self.state = 23
            self.match(MissionControlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MissionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MISSION(self):
            return self.getToken(MissionControlParser.MISSION, 0)

        def STRING(self):
            return self.getToken(MissionControlParser.STRING, 0)

        def LBRACE(self):
            return self.getToken(MissionControlParser.LBRACE, 0)

        def settingsBlock(self):
            return self.getTypedRuleContext(MissionControlParser.SettingsBlockContext,0)


        def waypointsBlock(self):
            return self.getTypedRuleContext(MissionControlParser.WaypointsBlockContext,0)


        def startBlock(self):
            return self.getTypedRuleContext(MissionControlParser.StartBlockContext,0)


        def endBlock(self):
            return self.getTypedRuleContext(MissionControlParser.EndBlockContext,0)


        def RBRACE(self):
            return self.getToken(MissionControlParser.RBRACE, 0)

        def taskBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MissionControlParser.TaskBlockContext)
            else:
                return self.getTypedRuleContext(MissionControlParser.TaskBlockContext,i)


        def getRuleIndex(self):
            return MissionControlParser.RULE_missionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMissionBlock" ):
                listener.enterMissionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMissionBlock" ):
                listener.exitMissionBlock(self)




    def missionBlock(self):

        localctx = MissionControlParser.MissionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_missionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(MissionControlParser.MISSION)
            self.state = 26
            self.match(MissionControlParser.STRING)
            self.state = 27
            self.match(MissionControlParser.LBRACE)
            self.state = 28
            self.settingsBlock()
            self.state = 29
            self.waypointsBlock()
            self.state = 30
            self.startBlock()
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 31
                self.taskBlock()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.endBlock()
            self.state = 38
            self.match(MissionControlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SettingsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SETTINGS(self):
            return self.getToken(MissionControlParser.SETTINGS, 0)

        def LBRACE(self):
            return self.getToken(MissionControlParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MissionControlParser.RBRACE, 0)

        def settingsEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MissionControlParser.SettingsEntryContext)
            else:
                return self.getTypedRuleContext(MissionControlParser.SettingsEntryContext,i)


        def getRuleIndex(self):
            return MissionControlParser.RULE_settingsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSettingsBlock" ):
                listener.enterSettingsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSettingsBlock" ):
                listener.exitSettingsBlock(self)




    def settingsBlock(self):

        localctx = MissionControlParser.SettingsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_settingsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MissionControlParser.SETTINGS)
            self.state = 41
            self.match(MissionControlParser.LBRACE)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 42
                self.settingsEntry()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(MissionControlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SettingsEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MissionControlParser.ID, 0)

        def COLON(self):
            return self.getToken(MissionControlParser.COLON, 0)

        def NUMBER(self):
            return self.getToken(MissionControlParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(MissionControlParser.FLOAT, 0)

        def COMMA(self):
            return self.getToken(MissionControlParser.COMMA, 0)

        def getRuleIndex(self):
            return MissionControlParser.RULE_settingsEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSettingsEntry" ):
                listener.enterSettingsEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSettingsEntry" ):
                listener.exitSettingsEntry(self)




    def settingsEntry(self):

        localctx = MissionControlParser.SettingsEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_settingsEntry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(MissionControlParser.ID)
            self.state = 51
            self.match(MissionControlParser.COLON)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==21 or _la==22):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 53
                self.match(MissionControlParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaypointsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAYPOINTS(self):
            return self.getToken(MissionControlParser.WAYPOINTS, 0)

        def LBRACE(self):
            return self.getToken(MissionControlParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MissionControlParser.RBRACE, 0)

        def waypointEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MissionControlParser.WaypointEntryContext)
            else:
                return self.getTypedRuleContext(MissionControlParser.WaypointEntryContext,i)


        def getRuleIndex(self):
            return MissionControlParser.RULE_waypointsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaypointsBlock" ):
                listener.enterWaypointsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaypointsBlock" ):
                listener.exitWaypointsBlock(self)




    def waypointsBlock(self):

        localctx = MissionControlParser.WaypointsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_waypointsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(MissionControlParser.WAYPOINTS)
            self.state = 57
            self.match(MissionControlParser.LBRACE)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 58
                self.waypointEntry()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(MissionControlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaypointEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MissionControlParser.STRING, 0)

        def COLON(self):
            return self.getToken(MissionControlParser.COLON, 0)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(MissionControlParser.FLOAT)
            else:
                return self.getToken(MissionControlParser.FLOAT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MissionControlParser.COMMA)
            else:
                return self.getToken(MissionControlParser.COMMA, i)

        def getRuleIndex(self):
            return MissionControlParser.RULE_waypointEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaypointEntry" ):
                listener.enterWaypointEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaypointEntry" ):
                listener.exitWaypointEntry(self)




    def waypointEntry(self):

        localctx = MissionControlParser.WaypointEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_waypointEntry)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(MissionControlParser.STRING)
            self.state = 67
            self.match(MissionControlParser.COLON)
            self.state = 68
            self.match(MissionControlParser.FLOAT)
            self.state = 69
            self.match(MissionControlParser.COMMA)
            self.state = 70
            self.match(MissionControlParser.FLOAT)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(MissionControlParser.COMMA)
                self.state = 72
                self.match(MissionControlParser.FLOAT)


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 75
                self.match(MissionControlParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START(self):
            return self.getToken(MissionControlParser.START, 0)

        def LBRACE(self):
            return self.getToken(MissionControlParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MissionControlParser.RBRACE, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MissionControlParser.CommandContext)
            else:
                return self.getTypedRuleContext(MissionControlParser.CommandContext,i)


        def getRuleIndex(self):
            return MissionControlParser.RULE_startBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartBlock" ):
                listener.enterStartBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartBlock" ):
                listener.exitStartBlock(self)




    def startBlock(self):

        localctx = MissionControlParser.StartBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_startBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MissionControlParser.START)
            self.state = 79
            self.match(MissionControlParser.LBRACE)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 80
                self.command()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(MissionControlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TaskBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TASK(self):
            return self.getToken(MissionControlParser.TASK, 0)

        def STRING(self):
            return self.getToken(MissionControlParser.STRING, 0)

        def LBRACE(self):
            return self.getToken(MissionControlParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MissionControlParser.RBRACE, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MissionControlParser.CommandContext)
            else:
                return self.getTypedRuleContext(MissionControlParser.CommandContext,i)


        def getRuleIndex(self):
            return MissionControlParser.RULE_taskBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTaskBlock" ):
                listener.enterTaskBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTaskBlock" ):
                listener.exitTaskBlock(self)




    def taskBlock(self):

        localctx = MissionControlParser.TaskBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_taskBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(MissionControlParser.TASK)
            self.state = 89
            self.match(MissionControlParser.STRING)
            self.state = 90
            self.match(MissionControlParser.LBRACE)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 91
                self.command()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(MissionControlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END(self):
            return self.getToken(MissionControlParser.END, 0)

        def LBRACE(self):
            return self.getToken(MissionControlParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MissionControlParser.RBRACE, 0)

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MissionControlParser.CommandContext)
            else:
                return self.getTypedRuleContext(MissionControlParser.CommandContext,i)


        def getRuleIndex(self):
            return MissionControlParser.RULE_endBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndBlock" ):
                listener.enterEndBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndBlock" ):
                listener.exitEndBlock(self)




    def endBlock(self):

        localctx = MissionControlParser.EndBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_endBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(MissionControlParser.END)
            self.state = 100
            self.match(MissionControlParser.LBRACE)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 126) != 0):
                self.state = 101
                self.command()
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self.match(MissionControlParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MissionControlParser.RULE_command

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CmdLandContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MissionControlParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MissionControlParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MissionControlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdLand" ):
                listener.enterCmdLand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdLand" ):
                listener.exitCmdLand(self)


    class CmdRTLContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MissionControlParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MissionControlParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MissionControlParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdRTL" ):
                listener.enterCmdRTL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdRTL" ):
                listener.exitCmdRTL(self)


    class CmdHoverContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MissionControlParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MissionControlParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MissionControlParser.RPAREN, 0)
        def NUMBER(self):
            return self.getToken(MissionControlParser.NUMBER, 0)
        def FLOAT(self):
            return self.getToken(MissionControlParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdHover" ):
                listener.enterCmdHover(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdHover" ):
                listener.exitCmdHover(self)


    class CmdTakeoffContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MissionControlParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MissionControlParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MissionControlParser.RPAREN, 0)
        def NUMBER(self):
            return self.getToken(MissionControlParser.NUMBER, 0)
        def FLOAT(self):
            return self.getToken(MissionControlParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdTakeoff" ):
                listener.enterCmdTakeoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdTakeoff" ):
                listener.exitCmdTakeoff(self)


    class CmdGotoContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MissionControlParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MissionControlParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MissionControlParser.RPAREN, 0)
        def STRING(self):
            return self.getToken(MissionControlParser.STRING, 0)
        def geoCoords(self):
            return self.getTypedRuleContext(MissionControlParser.GeoCoordsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdGoto" ):
                listener.enterCmdGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdGoto" ):
                listener.exitCmdGoto(self)


    class CmdSpeedContext(CommandContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MissionControlParser.CommandContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MissionControlParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MissionControlParser.RPAREN, 0)
        def NUMBER(self):
            return self.getToken(MissionControlParser.NUMBER, 0)
        def FLOAT(self):
            return self.getToken(MissionControlParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdSpeed" ):
                listener.enterCmdSpeed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdSpeed" ):
                listener.exitCmdSpeed(self)



    def command(self):

        localctx = MissionControlParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_command)
        self._la = 0 # Token type
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = MissionControlParser.CmdTakeoffContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(MissionControlParser.T__0)
                self.state = 110
                self.match(MissionControlParser.LPAREN)
                self.state = 111
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.match(MissionControlParser.RPAREN)
                pass
            elif token in [2]:
                localctx = MissionControlParser.CmdLandContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(MissionControlParser.T__1)
                self.state = 114
                self.match(MissionControlParser.LPAREN)
                self.state = 115
                self.match(MissionControlParser.RPAREN)
                pass
            elif token in [3]:
                localctx = MissionControlParser.CmdRTLContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 116
                self.match(MissionControlParser.T__2)
                self.state = 117
                self.match(MissionControlParser.LPAREN)
                self.state = 118
                self.match(MissionControlParser.RPAREN)
                pass
            elif token in [4]:
                localctx = MissionControlParser.CmdGotoContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 119
                self.match(MissionControlParser.T__3)
                self.state = 120
                self.match(MissionControlParser.LPAREN)
                self.state = 123
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 121
                    self.match(MissionControlParser.STRING)
                    pass
                elif token in [21]:
                    self.state = 122
                    self.geoCoords()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 125
                self.match(MissionControlParser.RPAREN)
                pass
            elif token in [5]:
                localctx = MissionControlParser.CmdHoverContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.match(MissionControlParser.T__4)
                self.state = 127
                self.match(MissionControlParser.LPAREN)
                self.state = 128
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 129
                self.match(MissionControlParser.RPAREN)
                pass
            elif token in [6]:
                localctx = MissionControlParser.CmdSpeedContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.match(MissionControlParser.T__5)
                self.state = 131
                self.match(MissionControlParser.LPAREN)
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.match(MissionControlParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeoCoordsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(MissionControlParser.FLOAT)
            else:
                return self.getToken(MissionControlParser.FLOAT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MissionControlParser.COMMA)
            else:
                return self.getToken(MissionControlParser.COMMA, i)

        def getRuleIndex(self):
            return MissionControlParser.RULE_geoCoords

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeoCoords" ):
                listener.enterGeoCoords(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeoCoords" ):
                listener.exitGeoCoords(self)




    def geoCoords(self):

        localctx = MissionControlParser.GeoCoordsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_geoCoords)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(MissionControlParser.FLOAT)
            self.state = 137
            self.match(MissionControlParser.COMMA)
            self.state = 138
            self.match(MissionControlParser.FLOAT)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 139
                self.match(MissionControlParser.COMMA)
                self.state = 140
                self.match(MissionControlParser.FLOAT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





