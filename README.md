# MissionControl DSL Compiler

Compilador para a Domain-Specific Language (DSL) **MissionControl**, focado em gerar missões autônomas para drones via MAVSDK.

## Estrutura
- `golden_target.py`: Script Python manual ("gabarito") validado no simulador. Serve de alvo para o gerador de código.
- `compiler/`: Código fonte do compilador (em desenvolvimento).

## Requisitos
- Python 3.10+
- MAVSDK
- ArduPilot SITL (Simulador)

## Como rodar o Golden Target (Teste de Prova de Conceito)
1. Inicie o simulador ArduPilot:
   ```bash
   sim_vehicle.py -v ArduCopter --console --map
   ```

2. Intale as dependências:
    ```bash
    pip install mavsdk
    ```

3. Execute o script
    ```bash
    python golden_target.py
    ```
