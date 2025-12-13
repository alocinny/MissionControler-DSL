# Guia Completo: Simulador e Execução (Windows)

Este guia cobre a instalação do simulador (via Mission Planner) e a execução dos scripts gerados pelo compilador.

## Parte 1: Instalação e Configuração do Simulador

A maneira mais simples de rodar o ArduPilot SITL (Software In The Loop) no Windows é através do Mission Planner.

1.  **Baixe o Mission Planner**:
    * Link oficial: [Mission Planner Installer (MSI)](https://firmware.ardupilot.org/Tools/MissionPlanner/MissionPlanner-latest.msi)

2.  **Instale o software**:
    * Execute o arquivo `.msi`.
    * Siga o assistente de instalação (Next > Next > Finish).
    * Se solicitado, aceite a instalação dos drivers de dispositivo.

3.  **Abra o Mission Planner**:
    * Ao abrir, se ele pedir para fazer atualizações, pode aceitar ou cancelar (não interfere na simulação básica).

4.  **Inicie a Simulação**:
    * No menu superior, clique no ícone **Simulation** (pode estar dentro de uma aba ou ícone de "Simulação").
    * Na lista de modelos, escolha **Multirotor** (ícone do drone).
    * Clique no link/botão **Plane/Quad** (ou "Stable").
    * O download do firmware iniciará automaticamente.
    * **Confirmação:** O drone aparecerá no mapa e uma janela de console (MAVProxy) abrirá. O simulador está pronto e escutando na porta **TCP 5760**.

---

## Parte 2: Executando a Missão Gerada

Agora que o drone virtual está voando, vamos conectar o script Python gerado por nossa DSL.

**Pré-requisitos**: Python 3.10+ instalado.

1.  **Abra o PowerShell** na pasta onde está o arquivo gerado (ex: `missoes_geradas/`).

2.  **Configure o ambiente Python** (caso ainda não tenha feito):
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    pip install mavsdk
    ```

3.  **Execute o script**:
    * *Nota: O simulador do Mission Planner geralmente usa a porta 5760. Se o script não conectar, verifique se a string de conexão no código Python é `tcp://127.0.0.1:5760`.*
    ```powershell
    python nome_da_sua_missao.py
    ```

4.  **Visualize**:
    * Acompanhe os comandos no terminal.
    * Veja o drone se movendo no mapa do Mission Planner.