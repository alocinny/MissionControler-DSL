import asyncio
from mavsdk import System

# waypoints extraídos da missão: Teste Missao Longa
WAYPOINTS = {'Home': {'lat': -27.6037, 'lon': -48.5191, 'alt': 0.0}, 'Ponto 1': {'lat': -27.58, 'lon': -48.56, 'alt': 35.0}, 'Ponto 2': {'lat': -27.575, 'lon': -48.55, 'alt': 30.0}, 'Ponto Check': {'lat': -27.585, 'lon': -48.54, 'alt': 25.0}, 'Ponto Final': {'lat': -27.59, 'lon': -48.53, 'alt': 20.0}}

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
    print('decolando para 20.0m...')
    await drone.action.arm()
    await drone.action.takeoff()
    await asyncio.sleep(10)
    print('    iniciando Task: "Percurso Longo"    ')
    print('indo para waypoint: Ponto 1')
    wp = WAYPOINTS['Ponto 1']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('indo para waypoint: Ponto 2')
    wp = WAYPOINTS['Ponto 2']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('hover por 5s...')
    await asyncio.sleep(5)
    print('indo para waypoint: Ponto Check')
    wp = WAYPOINTS['Ponto Check']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('    iniciando Task: "Retorno Programado"    ')
    print('indo para waypoint: Ponto Final')
    wp = WAYPOINTS['Ponto Final']
    await drone.action.goto_location(wp['lat'], wp['lon'], absolute_home_alt + wp['alt'], 0)
    await asyncio.sleep(8)
    print('hover por 10s...')
    await asyncio.sleep(10)
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
