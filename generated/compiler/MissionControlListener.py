# Generated from compiler/MissionControl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MissionControlParser import MissionControlParser
else:
    from MissionControlParser import MissionControlParser

# This class defines a complete listener for a parse tree produced by MissionControlParser.
class MissionControlListener(ParseTreeListener):

    # Enter a parse tree produced by MissionControlParser#prog.
    def enterProg(self, ctx:MissionControlParser.ProgContext):
        pass

    # Exit a parse tree produced by MissionControlParser#prog.
    def exitProg(self, ctx:MissionControlParser.ProgContext):
        pass


    # Enter a parse tree produced by MissionControlParser#missionBlock.
    def enterMissionBlock(self, ctx:MissionControlParser.MissionBlockContext):
        pass

    # Exit a parse tree produced by MissionControlParser#missionBlock.
    def exitMissionBlock(self, ctx:MissionControlParser.MissionBlockContext):
        pass


    # Enter a parse tree produced by MissionControlParser#settingsBlock.
    def enterSettingsBlock(self, ctx:MissionControlParser.SettingsBlockContext):
        pass

    # Exit a parse tree produced by MissionControlParser#settingsBlock.
    def exitSettingsBlock(self, ctx:MissionControlParser.SettingsBlockContext):
        pass


    # Enter a parse tree produced by MissionControlParser#settingsEntry.
    def enterSettingsEntry(self, ctx:MissionControlParser.SettingsEntryContext):
        pass

    # Exit a parse tree produced by MissionControlParser#settingsEntry.
    def exitSettingsEntry(self, ctx:MissionControlParser.SettingsEntryContext):
        pass


    # Enter a parse tree produced by MissionControlParser#waypointsBlock.
    def enterWaypointsBlock(self, ctx:MissionControlParser.WaypointsBlockContext):
        pass

    # Exit a parse tree produced by MissionControlParser#waypointsBlock.
    def exitWaypointsBlock(self, ctx:MissionControlParser.WaypointsBlockContext):
        pass


    # Enter a parse tree produced by MissionControlParser#waypointEntry.
    def enterWaypointEntry(self, ctx:MissionControlParser.WaypointEntryContext):
        pass

    # Exit a parse tree produced by MissionControlParser#waypointEntry.
    def exitWaypointEntry(self, ctx:MissionControlParser.WaypointEntryContext):
        pass


    # Enter a parse tree produced by MissionControlParser#startBlock.
    def enterStartBlock(self, ctx:MissionControlParser.StartBlockContext):
        pass

    # Exit a parse tree produced by MissionControlParser#startBlock.
    def exitStartBlock(self, ctx:MissionControlParser.StartBlockContext):
        pass


    # Enter a parse tree produced by MissionControlParser#taskBlock.
    def enterTaskBlock(self, ctx:MissionControlParser.TaskBlockContext):
        pass

    # Exit a parse tree produced by MissionControlParser#taskBlock.
    def exitTaskBlock(self, ctx:MissionControlParser.TaskBlockContext):
        pass


    # Enter a parse tree produced by MissionControlParser#endBlock.
    def enterEndBlock(self, ctx:MissionControlParser.EndBlockContext):
        pass

    # Exit a parse tree produced by MissionControlParser#endBlock.
    def exitEndBlock(self, ctx:MissionControlParser.EndBlockContext):
        pass


    # Enter a parse tree produced by MissionControlParser#CmdTakeoff.
    def enterCmdTakeoff(self, ctx:MissionControlParser.CmdTakeoffContext):
        pass

    # Exit a parse tree produced by MissionControlParser#CmdTakeoff.
    def exitCmdTakeoff(self, ctx:MissionControlParser.CmdTakeoffContext):
        pass


    # Enter a parse tree produced by MissionControlParser#CmdLand.
    def enterCmdLand(self, ctx:MissionControlParser.CmdLandContext):
        pass

    # Exit a parse tree produced by MissionControlParser#CmdLand.
    def exitCmdLand(self, ctx:MissionControlParser.CmdLandContext):
        pass


    # Enter a parse tree produced by MissionControlParser#CmdRTL.
    def enterCmdRTL(self, ctx:MissionControlParser.CmdRTLContext):
        pass

    # Exit a parse tree produced by MissionControlParser#CmdRTL.
    def exitCmdRTL(self, ctx:MissionControlParser.CmdRTLContext):
        pass


    # Enter a parse tree produced by MissionControlParser#CmdGoto.
    def enterCmdGoto(self, ctx:MissionControlParser.CmdGotoContext):
        pass

    # Exit a parse tree produced by MissionControlParser#CmdGoto.
    def exitCmdGoto(self, ctx:MissionControlParser.CmdGotoContext):
        pass


    # Enter a parse tree produced by MissionControlParser#CmdHover.
    def enterCmdHover(self, ctx:MissionControlParser.CmdHoverContext):
        pass

    # Exit a parse tree produced by MissionControlParser#CmdHover.
    def exitCmdHover(self, ctx:MissionControlParser.CmdHoverContext):
        pass


    # Enter a parse tree produced by MissionControlParser#CmdSpeed.
    def enterCmdSpeed(self, ctx:MissionControlParser.CmdSpeedContext):
        pass

    # Exit a parse tree produced by MissionControlParser#CmdSpeed.
    def exitCmdSpeed(self, ctx:MissionControlParser.CmdSpeedContext):
        pass


    # Enter a parse tree produced by MissionControlParser#geoCoords.
    def enterGeoCoords(self, ctx:MissionControlParser.GeoCoordsContext):
        pass

    # Exit a parse tree produced by MissionControlParser#geoCoords.
    def exitGeoCoords(self, ctx:MissionControlParser.GeoCoordsContext):
        pass



del MissionControlParser