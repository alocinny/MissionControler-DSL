from antlr4 import *
from MissionControlLexer import *
from MissionControlParser import *

# tabela de simbolos
tabela_simbolos = {
    "waypoints": set(),
    "tasks": set(),
    "settings": {
        "max_altitude": 100.0, # valor default
        "failsafe_battery": 10.0,
        "base_speed": 5.0
    }
}

# contexto atual pra validacao do takeoff
contexto_atual = None

def analise(t):
    global contexto_atual
    
    # caso de no vazio ou terminal
    if t is None or isinstance(t, TerminalNode):
        return

    match t:

        case MissionControlParser.ProgContext():
            analise(t.missionBlock())

        case MissionControlParser.MissionBlockContext():
            # processa filhos na ordem
            analise(t.settingsBlock())
            analise(t.waypointsBlock())
            analise(t.startBlock())
            for task in t.taskBlock():
                analise(task)
            analise(t.endBlock())

        case MissionControlParser.SettingsBlockContext():
            for entry in t.settingsEntry():
                analise(entry)

        case MissionControlParser.SettingsEntryContext():
            chave = t.ID().getText()
            valor = float(t.NUMBER().getText()) if t.NUMBER() else float(t.FLOAT().getText())

            # validacao semanticas de settings
            if chave == "failsafe_battery":
                if not (10 <= valor <= 30):
                    raise Exception(f"Erro Semântico: 'failsafe_battery' deve estar entre 10 e 30")
            
            if chave == "max_altitude" and valor <= 0:
                raise Exception(f"Erro Semântico: 'max_altitude' deve ser positivo.")

            
            tabela_simbolos["settings"][chave] = valor

        case MissionControlParser.WaypointsBlockContext():
            for entry in t.waypointEntry():
                analise(entry)

        case MissionControlParser.WaypointEntryContext():
            nome = t.STRING().getText().replace('"', '')
            coords = [float(x.getText()) for x in t.FLOAT()]
            lat, lon = coords[0], coords[1]
            alt = coords[2] if len(coords) > 2 else 0.0

            # validacao geografica
            if not (-90 <= lat <= 90):
                raise Exception(f"Erro Semântico: Latitude inválida")
            if not (-180 <= lon <= 180):
                raise Exception(f"Erro Semântico: Longitude inválida")

            # Validacao de unicidade
            if nome in tabela_simbolos["waypoints"]:
                raise Exception(f"Erro Semântico: Waypoint '{nome}' duplicado.")
            
            tabela_simbolos["waypoints"].add(nome)

        case MissionControlParser.StartBlockContext():
            contexto_atual = "START"
            for cmd in t.command():
                analise(cmd)
            contexto_atual = None

        case MissionControlParser.TaskBlockContext():
            nome_task = t.STRING().getText().replace('"', '')
            if nome_task in tabela_simbolos["tasks"]:
                raise Exception(f"Erro Semântico: Task '{nome_task}' duplicada.")
            tabela_simbolos["tasks"].add(nome_task)
            
            contexto_atual = "TASK"
            for cmd in t.command():
                analise(cmd)
            contexto_atual = None

        case MissionControlParser.EndBlockContext():
            contexto_atual = "END"
            for cmd in t.command():
                analise(cmd)
            contexto_atual = None

        # comandos
        
        case MissionControlParser.CmdTakeoffContext():
            if contexto_atual != "START":
                raise Exception("Erro Semântico: 'takeoff' só é permitido no bloco 'start'.")
            
            alt = float(t.NUMBER().getText()) if t.NUMBER() else float(t.FLOAT().getText())
            max_alt = tabela_simbolos["settings"]["max_altitude"]
            
            if alt > max_alt:
                raise Exception(f"Erro de Segurança: Decolagem excede o valor máximo")

        case MissionControlParser.CmdGotoContext():
            # verifica se e navegacao por nome ou coordenadas
            if t.STRING():
                wp_nome = t.STRING().getText().replace('"', '')
                if wp_nome not in tabela_simbolos["waypoints"]:
                    raise Exception(f"Erro Semântico: Waypoint não definido.")
            else:
                pass 

        case MissionControlParser.CmdHoverContext():
            val = float(t.NUMBER().getText()) if t.NUMBER() else float(t.FLOAT().getText())
            if val <= 0:
                raise Exception("Erro Semântico: Tempo de hover deve ser positivo.")

        case _:
            # percorre filhos caso nao caia em nenhum case especifico
            if hasattr(t, 'getChildren'):
                for child in t.getChildren():
                    analise(child)