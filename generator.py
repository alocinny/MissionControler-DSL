class MissionCodeGenerator:
    def __init__(self, ir):
        self.ir = ir
        self.indent = "    "  # 4 espaços

    def generate(self):
        sections = []
        sections.append(self._generate_imports())
        sections.append(self._generate_waypoints())
        sections.append(self._generate_run_function())
        sections.append(self._generate_main_block())
        return "\n".join(sections)

    def _generate_imports(self):
        return """import asyncio
from mavsdk import System
"""

    def _generate_waypoints(self):
        return f"\n# Dicionário de Waypoints\nWAYPOINTS = {repr(self.ir['waypoints'])}\n"

    def _generate_run_function(self):
        # Boilerplate de Conexão e Setup (Estático)
        setup_code = f"""
async def run():

    drone = System()
    print("-- [GEN] Conectando ao drone...")
    await drone.connect(system_address="udp://:14540")

    print("-- [GEN] Aguardando heartbeat...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- [GEN] Drone conectado!")
            break

    # Solução de Segurança: Desativa checagens pré-voo para facilitar simulação
    print("-- [SETUP] Desativando Pre-Arm Checks (ARMING_CHECK=0)...")
    try:
        await drone.param.set_param_int("ARMING_CHECK", 0)
    except Exception as e:
        print(f"-- Aviso: Falha ao setar parâmetro: {{e}}")

    # --- 2. VERIFICAÇÕES DE GPS E TERRENO ---
    print("-- [GPS] Aguardando 3D Lock...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- [GPS] Posição Global OK.")
            break

    print("-- [GPS] Calculando altitude absoluta do terreno (Home)...")
    absolute_home_alt = 0
    async for terrain_info in drone.telemetry.home():
        absolute_home_alt = terrain_info.absolute_altitude_m
        break
    print(f"-- [GPS] Home Altitude: {{absolute_home_alt}}m AMSL")

    # --- 3. EXECUÇÃO DA MISSÃO: {self.ir['mission_name']} ---
"""
        
        # Tradução Dinâmica dos Comandos
        commands_code = []
        
        for cmd in self.ir["commands"]:
            commands_code.extend(self._translate_command(cmd))

        return setup_code + "\n".join(commands_code)

    def _translate_command(self, cmd):
        lines = []
        
        if cmd["type"] == "TAKEOFF":
            alt = cmd["alt"]
            lines.append(f"{self.indent}print('-- [CMD] Armando motores...')")
            lines.append(f"{self.indent}await drone.action.arm()")
            
            # Loop de confirmação de Arm
            lines.append(f"{self.indent}print('-- [CMD] Confirmando armamento...')")
            lines.append(f"{self.indent}async for armed in drone.telemetry.armed():")
            lines.append(f"{self.indent}{self.indent}if armed: break")
            
            lines.append(f"{self.indent}print(f'-- [CMD] Decolando para {alt}m...')")
            lines.append(f"{self.indent}await drone.action.set_takeoff_altitude({alt})")
            lines.append(f"{self.indent}await drone.action.takeoff()")
            lines.append(f"{self.indent}await asyncio.sleep(12) # Tempo para subir")

        elif cmd["type"] == "LAND":
            lines.append(f"{self.indent}print('-- [CMD] Pousando (Land)...')")
            lines.append(f"{self.indent}try:")
            lines.append(f"{self.indent}{self.indent}await drone.action.land()")
            lines.append(f"{self.indent}except Exception as e: print(f'-- Aviso Land: {{e}}')")

        elif cmd["type"] == "HOVER":
            dur = cmd["duration"]
            lines.append(f"{self.indent}print(f'-- [CMD] Hover por {dur}s...')")
            lines.append(f"{self.indent}await asyncio.sleep({dur})")

        elif cmd["type"] == "SPEED":
            val = cmd["val"]
            lines.append(f"{self.indent}print(f'-- [CMD] Ajustando velocidade: {val}m/s')")
            lines.append(f"{self.indent}await drone.action.set_maximum_speed({val})")
        

        elif cmd["type"] == "goto":
            # Lógica Inteligente de Altitude Absoluta
            if "wp_name" in cmd:
                wp_name = cmd["wp_name"]
                lines.append(f"{self.indent}wp = WAYPOINTS['{wp_name}']")
                lines.append(f"{self.indent}tgt_alt = absolute_home_alt + wp['alt']")
                lines.append(f"{self.indent}print(f'-> Indo para {wp_name} (Lat:{{wp[\"lat\"]}}, Lon:{{wp[\"lon\"]}}, Alt AMSL:{{tgt_alt}})')")
                lines.append(f"{self.indent}await drone.action.goto_location(wp['lat'], wp['lon'], tgt_alt, 0)")
            else:
                lat, lon, alt = cmd["lat"], cmd["lon"], cmd["alt"]
                lines.append(f"{self.indent}tgt_alt = absolute_home_alt + {alt}")
                lines.append(f"{self.indent}print(f'-> Indo para Coord Fixa (Lat:{lat}, Lon:{lon}, Alt AMSL:{{tgt_alt}})')")
                lines.append(f"{self.indent}await drone.action.goto_location({lat}, {lon}, tgt_alt, 0)")
            
            # Sleep para simular tempo de voo 
            lines.append(f"{self.indent}await asyncio.sleep(8)")
        
        elif cmd.get("type") == "RTL": 
             lines.append(f"{self.indent}print('-- [CMD] Retornando para casa (RTL)...')")
             lines.append(f"{self.indent}await drone.action.return_to_launch()")
             lines.append(f"{self.indent}await asyncio.sleep(15)")

        return lines

    def _generate_main_block(self):
        return """
    print("--- MISSÃO CONCLUÍDA ---")

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("Cancelado pelo usuário.")
"""