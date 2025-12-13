import asyncio
from mavsdk import System

# waypoints extraídos da missão: Teste Missao Loop
WAYPOINTS = {'Home': {'lat': -27.6037, 'lon': -48.5191, 'alt': 0.0}, 'Inspecao A': {'lat': -27.591, 'lon': -48.551, 'alt': 10.0}, 'Inspecao B': {'lat': -27.592, 'lon': -48.552, 'alt': 10.0}}

async def run():
    drone = System()
    await drone.connect(system_address='udp://:14540')
    print('conectado ao drone')
    # configuração de Home
    absolute_home_alt = 0
    async for terrain_info in drone.telemetry.home():
        absolute_home_alt = terrain_info.absolute_altitude_m
        break

    #     inicio da execução    
    print('decolando para 8.0m...')
    await drone.action.arm()
    await drone.action.takeoff()
    await asyncio.sleep(10)
    print('    iniciando Task: "Ciclo de Inspecao"    ')
    print('indo para waypoint: Inspecao A')
    wp = WAYPOINTS['Inspecao A']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('hover por 3s...')
    await asyncio.sleep(3)
    print('indo para waypoint: Inspecao B')
    wp = WAYPOINTS['Inspecao B']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('hover por 3s...')
    await asyncio.sleep(3)
    print('indo para waypoint: Inspecao A')
    wp = WAYPOINTS['Inspecao A']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('hover por 3s...')
    await asyncio.sleep(3)
    print('indo para waypoint: Inspecao B')
    wp = WAYPOINTS['Inspecao B']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('hover por 3s...')
    await asyncio.sleep(3)
    print('    iniciando Task: "Voltar para Base"    ')
    print('retornando para casa (RTL)...')
    await drone.action.return_to_launch()
    print('    finalizando Missão    ')
    print('pousando...')
    await drone.action.land()
    print('missão finalizada')

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run())
