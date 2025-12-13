# MissionControl DSL Compiler

**Compilador de Missões Autónomas para Drones (MAVSDK/ArduPilot)**

Compilador para a Domain-Specific Language (DSL) **MissionControl**, focado em gerar missões autônomas para drones via MAVSDK.

Este projeto converte arquivos de missão (`.mc`) de alto nível em scripts Python executáveis, prontos para serem enviados a um *autopilot* (como ArduPilot) por meio da biblioteca MAVSDK.


## Motivação
A programação de missões autónomas para drones exige, tradicionalmente, um conhecimento profundo de protocolos complexos (MAVLink), bibliotecas assíncronas (como `asyncio` em Python) e gestão de estados de voo. Erros nestes scripts podem resultar em acidentes físicos dispendiosos.
A **MissionControl DSL** resolve este problema ao abstrair a complexidade técnica. Permite que operadores definam missões de forma **declarativa**, focando-se no "o quê" (waypoints, tarefas) em vez do "como" (código de baixo nível). O compilador garante ainda validações de segurança críticas (como bateria mínima e altitude máxima) *antes* de gerar o código final, prevenindo falhas catastróficas em tempo de execução.

---

## Estrutura do Projeto

MissionControl/
│
├── .devcontainer/              # 
├── exemplos/                   # Pasta contendo scripts de exemplo (.mc) para teste
├── missoes_geradas/            # Pasta de saída onde os arquivos compilados/gerados são salvos
│
├── MissionControl.g4           # Arquivo da gramática ANTLR4 (Lexer + Parser)
│
├── main.py                     # Ponto de entrada: lê o arquivo, chama o lexer/parser e inicia a compilação
├── analisador_semantico.py     # Lógica de validação semântica (verifica tipos, variáveis e regras de negócio)
├── compilador.py               # Backend: transforma a árvore sintática no código alvo 
│
├── MissionControlLexer.py      # Gerado pelo ANTLR: Transforma texto em tokens
├── MissionControlParser.py     # Gerado pelo ANTLR: Cria a árvore sintática a partir dos tokens
├── MissionControlListener.py   # Gerado pelo ANTLR: Interface para percorrer a árvore (padrão Listener)
│
├── requirements.txt            # Lista de dependências do projeto (ex: antlr4-python3-runtime)
└── README.md                   # Documentação do projeto

---


################## 




AQUI BENNY



################## 


## Equipe

* **[Ana Beatriz Soares]** 
* **[Danielle Stephany Nunes]** 
* **[Michelly Darquia]** 
* **[Pedro de Melo]** 

**Orientação:**
* **Prof. Luis Carlos**