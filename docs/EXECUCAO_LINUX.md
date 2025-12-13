# Guia Completo: Simulador e Execução (Linux)

Este guia cobre a instalação do ambiente de desenvolvimento ArduPilot (SITL) e a execução dos scripts.

## Parte 1: Instalação do Simulador (ArduPilot SITL)

1.  **Instale o Git** (caso não tenha):
    ```bash
    sudo apt update
    sudo apt install git
    ```

2.  **Clone o repositório do ArduPilot**:
    ```bash
    cd ~
    git clone --recurse-submodules [https://github.com/ArduPilot/ardupilot.git](https://github.com/ArduPilot/ardupilot.git)
    cd ardupilot
    ```

3.  **Execute o script de instalação de dependências**:
    * Este script instala automaticamente compiladores GCC, Python e MAVProxy.
    ```bash
    Tools/environment_install/install-prereqs-ubuntu.sh -y
    ```

4.  **Atualize as variáveis de ambiente**:
    ```bash
    . ~/.profile
    ```

5.  **Teste o Simulador**:
    * Este comando compila e inicia um drone (Copter) na localização padrão.
    ```bash
    cd ~/ardupilot/ArduCopter
    sim_vehicle.py -w
    ```
    * Se aparecer `GPS: 3D Fix` no console, o simulador está pronto. Pode fechar com `Ctrl+C`.

---

## Parte 2: Executando a Missão Gerada

**Pré-requisito**: Mantenha o terminal do simulador **fechado** antes de iniciar este passo, pois abriremos um novo.

1.  **Inicie o Simulador em um terminal**:
    ```bash
    sim_vehicle.py -v ArduCopter --console --map
    ```
    * Aguarde o drone inicializar totalmente.

2.  **Prepare o script da missão (em OUTRO terminal)**:
    * Navegue até a pasta do arquivo `.py` gerado.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install mavsdk
    ```

3.  **Execute a missão**:
    * O simulador Linux nativo geralmente escuta na porta UDP 14540.
    ```bash
    python3 nome_da_sua_missao.py
    ```

4.  **Visualize**:
    * O drone deve decolar e seguir os waypoints no mapa que abriu junto com o simulador.