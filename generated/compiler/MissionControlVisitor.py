# Generated from compiler/MissionControl.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MissionControlParser import MissionControlParser
else:
    from MissionControlParser import MissionControlParser

# This class defines a complete generic visitor for a parse tree produced by MissionControlParser.

class MissionControlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MissionControlParser#prog.
    def visitProg(self, ctx:MissionControlParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#missionBlock.
    def visitMissionBlock(self, ctx:MissionControlParser.MissionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#settingsBlock.
    def visitSettingsBlock(self, ctx:MissionControlParser.SettingsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#settingsEntry.
    def visitSettingsEntry(self, ctx:MissionControlParser.SettingsEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#waypointsBlock.
    def visitWaypointsBlock(self, ctx:MissionControlParser.WaypointsBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#waypointEntry.
    def visitWaypointEntry(self, ctx:MissionControlParser.WaypointEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#startBlock.
    def visitStartBlock(self, ctx:MissionControlParser.StartBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#taskBlock.
    def visitTaskBlock(self, ctx:MissionControlParser.TaskBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#endBlock.
    def visitEndBlock(self, ctx:MissionControlParser.EndBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#CmdTakeoff.
    def visitCmdTakeoff(self, ctx:MissionControlParser.CmdTakeoffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#CmdLand.
    def visitCmdLand(self, ctx:MissionControlParser.CmdLandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#CmdRTL.
    def visitCmdRTL(self, ctx:MissionControlParser.CmdRTLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#CmdGoto.
    def visitCmdGoto(self, ctx:MissionControlParser.CmdGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#CmdHover.
    def visitCmdHover(self, ctx:MissionControlParser.CmdHoverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#CmdSpeed.
    def visitCmdSpeed(self, ctx:MissionControlParser.CmdSpeedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MissionControlParser#geoCoords.
    def visitGeoCoords(self, ctx:MissionControlParser.GeoCoordsContext):
        return self.visitChildren(ctx)



del MissionControlParser