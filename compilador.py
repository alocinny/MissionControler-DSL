from antlr4 import *
from MissionControlLexer import *
from MissionControlParser import *

waypoints_data = {} 
mission_name = "Missao"

def gera_codigo(t):
    global waypoints_data, mission_name

    match t:

        case MissionControlParser.ProgContext():
            gera_codigo(t.missionBlock())

        case MissionControlParser.MissionBlockContext():
            mission_name = t.STRING().getText().replace('"', '')
            
            _extrair_waypoints(t.waypointsBlock())

            print("import asyncio")
            print("from mavsdk import System")
            print("")
            print(f"# waypoints extraídos da missão: {mission_name}")
            print(f"WAYPOINTS = {repr(waypoints_data)}")
            print("")
            print("async def run():")
            print("    drone = System()")
            print("    await drone.connect(system_address='udp://:14540')")
            print("    print('conectado ao drone')")
            print("    # configuração de Home")
            print("    absolute_home_alt = 0")
            print("    async for terrain_info in drone.telemetry.home():")
            print("        absolute_home_alt = terrain_info.absolute_altitude_m")
            print("        break")
            print("")
            
            print("    #     inicio da execução    ")
            gera_codigo(t.startBlock())
            
            for task in t.taskBlock():
                gera_codigo(task)
                
            gera_codigo(t.endBlock())

            print("    print('missão finalizada')")
            print("")
            print("if __name__ == '__main__':")
            print("    loop = asyncio.new_event_loop()")
            print("    asyncio.set_event_loop(loop)")
            print("    loop.run_until_complete(run())")

        case MissionControlParser.StartBlockContext():
            for cmd in t.command():
                gera_codigo(cmd)

        case MissionControlParser.TaskBlockContext():
            print(f"    print('    iniciando Task: {t.STRING().getText()}    ')")
            for cmd in t.command():
                gera_codigo(cmd)

        case MissionControlParser.EndBlockContext():
            print("    print('    finalizando Missão    ')")
            for cmd in t.command():
                gera_codigo(cmd)

        case MissionControlParser.CmdTakeoffContext():
            alt = t.NUMBER().getText() if t.NUMBER() else t.FLOAT().getText()
            print(f"    print('decolando para {alt}m...')")
            print("    await drone.action.arm()")
            print(f"    await drone.action.takeoff()")
            print("    await asyncio.sleep(10)") 

        case MissionControlParser.CmdLandContext():
            print("    print('pousando...')")
            print("    await drone.action.land()")

        case MissionControlParser.CmdRTLContext():
            print("    print('retornando para casa (RTL)...')")
            print("    await drone.action.return_to_launch()")

        case MissionControlParser.CmdHoverContext():
            dur = t.NUMBER().getText() if t.NUMBER() else t.FLOAT().getText()
            print(f"    print('hover por {dur}s...')")
            print(f"    await asyncio.sleep({dur})")

        case MissionControlParser.CmdGotoContext():
            if t.STRING():
                wp_name = t.STRING().getText().replace('"', '')
                print(f"    print('indo para waypoint: {wp_name}')")
                print(f"    wp = WAYPOINTS['{wp_name}']")
                print(f"    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)")
            else:
                pass
            print("    await asyncio.sleep(8)")

        case _:
            pass

def _extrair_waypoints(ctx):
    global waypoints_data
    if not ctx: return
    
    for entry in ctx.waypointEntry():
        nome = entry.STRING().getText().replace('"', '')
        coords = [float(x.getText()) for x in entry.FLOAT()]
        waypoints_data[nome] = {
            "lat": coords[0],
            "lon": coords[1],
            "alt": coords[2] if len(coords) > 2 else 0.0
        }