import sys 
from generated.compiler.MissionControlVisitor import MissionControlVisitor
from generated.compiler.MissionControlParser import MissionControlParser

class MissionCompiler(MissionControlVisitor):
    def __init__(self):
        self.ir = {
            "mission_name": "",
            "settings": {},
            "waypoints": {},
            "commands": [] 
        }

        # tabela de simbolos
        self.symbol_table = {
            "defined_waypoints": set(),
            "defined_tasks": set()
        }

        self.current_block = None
    
    def visitStartBlock(self, ctx: MissionControlParser.StartBlockContext):
        self.current_block = "START"
        result = self.visitChildren(ctx)
        self.current_block = None
        return result
    
    def visitTaskBlock(self, ctx: MissionControlParser.TaskBlockContext):
        self.current_block = "TASK"

        # validar nome da task unico
        task_name = ctx.STRING().getText().replace('"','')
        if task_name in self.symbol_table["defined_tasks"]:
            raise Exception("task duplicada")
        self.symbol_table["defined_tasks"].add(task_name)

        result = self.visitChildren(ctx)
        self.current_block = None
        return result
    
    def visitEndBlock(self, ctx: MissionControlParser.EndBlockContext):
        self.current_block = "END"
        result = self.visitChildren(ctx)
        self.current_block = None
        return result
    

    def visitMissionBlock(self, ctx: MissionControlParser.MissionBlockContext):
        raw_name = ctx.STRING().getText()
        self.ir["mission_name"] = raw_name.replace('"','')

        return self.visitChildren(ctx)
    
    def visitSettingsEntry(self, ctx: MissionControlParser.SettingsEntryContext):
        key = ctx.ID().getText()

        if ctx.NUMBER():
            value = int(ctx.NUMBER().getText())
        else:
            value = float(ctx.FLOAT().getText())

        # analise semantica
        # regra do failsafe
        if key == "failsafe_battery":
            if not (10 <= value <= 30):
                raise Exception ("erro semantico: 'failsafe_battery' deve estar entre 10 e 30")
        
        if key == "max_altitude" and value <= 0:
            raise Exception(f"Erro semântico: 'max_altitude' deve ser positivo (recebi {value})")

        if key == "base_speed" and value <= 0:
            raise Exception(f"Erro semântico: 'base_speed' deve ser positiva (recebi {value})")

        self.ir["settings"][key] = value
        return self.visitChildren(ctx)

    def visitWaypointEntry(self, ctx: MissionControlParser.WaypointEntryContext):
        wp_name = ctx.STRING().getText().replace('"','')

        coords = [float(x.getText()) for x in ctx.FLOAT()]

        lat = coords[0]
        lon = coords[1]
        alt = coords[2] if len(coords) > 2 else 0.0 # pra deixar altitude opcional

        if not (-90 <= lat <= 90):
            raise Exception(f"Erro semântico: Latitude {lat} inválida (deve ser entre -90 e 90)")
        if not (-180 <= lon <= 180):
            raise Exception(f"Erro semântico: Longitude {lon} inválida (deve ser entre -180 e 180)")


        if wp_name in self.symbol_table["defined_waypoints"]:
            raise Exception("waypoint duplicado")
        
        self.symbol_table["defined_waypoints"].add(wp_name)

        self.ir["waypoints"][wp_name] = {"lat": lat, "lon": lon, "alt": alt}

        return self.visitChildren(ctx)
    
    def visitCmdTakeoff(self, ctx: MissionControlParser.CmdTakeoffContext):
        # so é permitido dentro do bloco start
        if self.current_block != "START":
            raise Exception("takeoff fora do bloco START")
        
        if ctx.NUMBER():
            alt = float(ctx.NUMBER().getText())
        else:
            alt = float(ctx.FLOAT().getText())

        # analise semantica
        # regra altitude maxima
        max_alt = self.ir["settings"].get("max_altitude", 100.0) # default 100 caso não esteja definido
        if alt > max_alt:
            raise Exception("altura maxima excedida")
        
        self.ir["commands"].append({"type": "TAKEOFF", "alt": alt})
        return self.visitChildren(ctx)
    
    def visitCmdGoto(self, ctx: MissionControlParser.CmdGotoContext):
        
        max_alt = self.ir["settings"].get("max_altitude", 100.0)
        # pode ser goto("nome") ou goto(lat, lon, alt)

        if ctx.STRING():
            wp_name = ctx.STRING().getText().replace('"','')
            
            if wp_name not in self.symbol_table["defined_waypoints"]:
                raise Exception("waypoint nao definido")

            self.ir["commands"].append({"type": "goto", "wp_name": wp_name})
            
            wp_alt = self.ir["waypoints"][wp_name]["alt"] # Busca a altitude desse waypoint no nosso IR para conferir
            if wp_alt > max_alt:
                raise Exception(f"Erro de Segurança: O waypoint '{wp_name}' tem altitude {wp_alt}m, que é maior que o máximo permitido ({max_alt}m).")

        else:
            coords = [float(x.getText()) for x in ctx.geoCoords().FLOAT()]
            lat, lon = coords[:2]
            alt = coords[2] if len(coords) > 2 else 0.0

            if not (-90 <= lat <= 90):
                raise Exception(f"Erro semântico: Latitude {lat} inválida (deve ser entre -90 e 90)")
            if not (-180 <= lon <= 180):
                raise Exception(f"Erro semântico: Longitude {lon} inválida (deve ser entre -180 e 180)")
            
            if alt > max_alt:
                raise Exception(f"Erro de Segurança: O comando goto tenta ir para {alt}m, mas o máximo permitido é {max_alt}m.")
            
            self.ir["commands"].append({"type": "goto", "lat": lat, "lon": lon, "alt": alt})
        
        return self.visitChildren(ctx)

    def visitCmdLand(self, ctx: MissionControlParser.CmdLandContext):
        self.ir["commands"].append({"type": "LAND"})
        return self.visitChildren(ctx)
    
    def visitCmdHover(self, ctx: MissionControlParser.CmdHoverContext):
        val = float(ctx.NUMBER().getText()) if ctx.NUMBER() else float(ctx.FLOAT().getText())

        if val <= 0:
            raise Exception(f"Erro semântico: O tempo de hover deve ser positivo (recebi {val})")

        self.ir["commands"].append({"type": "HOVER", "duration": val})
        return self.visitChildren(ctx)
    
    def visitCmdSpeed(self, ctx: MissionControlParser.CmdSpeedContext):
        val = float(ctx.NUMBER().getText()) if ctx.NUMBER() else float(ctx.FLOAT().getText())

        if val <= 0:
            raise Exception(f"Erro semântico: A velocidade deve ser maior que zero (recebi {val})")
        
        self.ir["commands"].append({"type": "SPEED", "val": val})
        return self.visitChildren(ctx)

        