# MissionControl DSL Compiler

Compilador para a Domain-Specific Language (DSL) **MissionControl**, focado em gerar missões autônomas para drones via MAVSDK.

Este projeto converte arquivos de missão (`.mc`) de alto nível em scripts Python executáveis, prontos para serem enviados a um *autopilot* (como ArduPilot) por meio da biblioteca MAVSDK.

---

## Estrutura do Projeto

* `*.mc`: Arquivos de entrada que definem a missão usando a sintaxe MissionControl DSL.
* `main.py`: Ponto de entrada do compilador.
* `compiler/`: Código fonte do compilador (Lexer, Parser, Visitor e Gerador de Código).
* **`build/`**: Diretório de saída onde os scripts Python gerados são salvos. **Este diretório é ignorado pelo Git.**

---

## Requisitos

Para rodar o compilador e executar as missões geradas, você precisará:

* **Python 3.10+**
* **MAVSDK** (Para comunicação com o drone/simulador)
* **ArduPilot SITL** (Software-in-the-Loop, um simulador de drone)

### Instalação de Dependências

Certifique-se de que todas as dependências Python necessárias estejam instaladas:

```bash
pip install mavsdk
pip install antlr4-python3-runtime
```

## Como Compilar e Rodar uma Missão

### 1. Compilar o Arquivo de Missão ( .mc )

Execute o `main.py`, passando o caminho para o seu arquivo de missão como argumento. O arquivo Python gerado será salvo automaticamente no diretório `build/`.

#### Comando de Compilação:

```bash
python main.py &lt;CAMINHO_PARA_ARQUIVO&gt;.mc
```

---

#### Exemplo: Se o arquivo de entrada for `missao_curta.mc`, a saída será:

- Sucesso! Arquivo 'build/missao_curta.py' gerado.
- Para rodar: python build/missao_curta.py

---

### 2. Iniciar o Simulador

Para testar a missão, inicie o simulador ArduPilot (SITL) em um terminal separado.

```bash
sim_vehicle.py -v ArduCopter --console --map
```

O simulador deve estar rodando e aguardando a conexão MAVSDK.

### 3. Executar o Script Gerado

Use o comando de execução fornecido na etapa de compilação. Este script Python irá se conectar ao simulador via MAVSDK e iniciar a missão.

#### Comando de Execução (Exemplo):

```bash
python build/missao_curta.py
```
