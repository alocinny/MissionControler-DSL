grammar MissionControl;

prog: missionBlock EOF;

missionBlock: 'mission' STRING LBRACE settingsBlock waypointsBlock startBlock taskBlock* endBlock RBRACE;

settingsBlock: 'settings' LBRACE settingsEntry* RBRACE;
settingsEntry: ID COLON (NUMBER | FLOAT) (COMMA)?;

waypointsBlock: 'waypoints' LBRACE waypointEntry* RBRACE;
waypointEntry: STRING COLON FLOAT COMMA FLOAT (COMMA FLOAT)? (COMMA)?;

startBlock: 'start' LBRACE command* RBRACE;

taskBlock: 'task' STRING LBRACE command* RBRACE;

endBlock: 'end' LBRACE command* RBRACE;

command:
    'takeoff' LPAREN (NUMBER|FLOAT) RPAREN # CmdTakeoff
    | 'land' LPAREN RPAREN # CmdLand
    | 'rtl' LPAREN RPAREN # CmdRTL
    | 'goto' LPAREN (STRING | geoCoords) RPAREN # CmdGoto
    | 'hover' LPAREN (NUMBER|FLOAT) RPAREN # CmdHover
    | 'speed' LPAREN (NUMBER|FLOAT) RPAREN #CmdSpeed
;

geoCoords: FLOAT COMMA FLOAT (COMMA FLOAT)?;

// ---

MISSION: 'mission';
SETTINGS: 'settings';
WAYPOINTS: 'waypoints';
START: 'start';
TASK: 'task';
END: 'end';

LBRACE: '{';
RBRACE: '}';
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"' ;
FLOAT: '-'? [0-9]+ '.' [0-9]+;
NUMBER: '-'? [0-9]+;
COMMENT: '#' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
