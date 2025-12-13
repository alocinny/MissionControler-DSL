# MissionControl DSL Compiler

Compilador de Missões Autónomas para Drones (MAVSDK/ArduPilot)

Compilador para a Domain-Specific Language (DSL) **MissionControl**, focado em gerar missões autônomas para drones via MAVSDK.

Este projeto converte arquivos de missão (`.mc`) de alto nível em scripts Python executáveis, prontos para serem enviados a um *autopilot* (como ArduPilot) por meio da biblioteca MAVSDK.


## Motivação
A programação de missões autonomas para drones exige, tradicionalmente, um conhecimento profundo de protocolos complexos (MAVLink), bibliotecas assíncronas (como `asyncio` em Python) e gestão de estados de voo. Erros nestes scripts podem resultar em acidentes físicos dispendiosos.

A **MissionControl DSL** resolve este problema ao abstrair a complexidade técnica. Permite que operadores definam missões de forma **declarativa**, focando-se no "o quê" (waypoints, tarefas) em vez do "como" (código de baixo nível). O compilador garante ainda validações de segurança críticas (como bateria mínima e altitude máxima) *antes* de gerar o código final, prevenindo falhas catastróficas em tempo de execução.


## Estrutura do Projeto

```text

MissionControl/
│
├── .devcontainer/              # Configurações para container
├── exemplos/                   # Pasta contendo scripts de exemplo (.mc) para teste
├── missoes_geradas/            # Pasta de saída: onde os arquivos compilados/gerados são salvos
│
├── MissionControl.g4           # Arquivo da gramática ANTLR4 (Lexer + Parser)
│
├── main.py                     # Ponto de entrada: lê o arquivo, chama o lexer/parser e inicia a compilação
├── analisador_semantico.py     # Lógica de validação semântica
├── compilador.py               # Backend: transforma a árvore sintática no código alvo 
│
├── MissionControlLexer.py      # Gerado pelo ANTLR: Transforma texto em tokens
├── MissionControlParser.py     # Gerado pelo ANTLR: Cria a árvore sintática a partir dos tokens
├── MissionControlListener.py   # Gerado pelo ANTLR: Interface para percorrer a árvore (padrão Listener)
│
├── requirements.txt            # Dependências
└── README.md                   # Documentação

```

## Execução via GitHub Codespaces

Esse projeto possui um ambiente de desenvolvimento em nuvem configurado.

1. No topo da página do repositório no GitHub, clique no botão `<> Code`
2. Selecione a aba **Codespaces**
3. Clique em **Create codespace on main**
4. Aguarde o ambiente carregar
    * *Nota:* O arquivo `.devContainer` instalará automaticamente o **Java 17** necessário para o ANTLR, **Python 3.1**, a extensão do VS Code para ANTLR e todas as dependências do `requirements.txt`
5. Assim que o terminal estiver disponível, execute o compilador:
    ```bash
    python main.py exemplos/<nome_do_arquivo_de_teste>.mc
    ```


## Execução Local

Caso prefira rodar o projeto na sua própria máquina (Windows, Linux ou Mac) em vez do Codespaces:

1. Pré-requisitos:

- Python 3.8 ou superior.
- Java (JRE ou JDK) instalado (necessário para o funcionamento do ANTLR).

2. Instalação das Dependências: No terminal, dentro da pasta do projeto, execute:
    ```bash
    pip install -r requirements.txt
    ```

3. Execução: Para compilar um arquivo, use o comando:
    ```bash
    python main.py exemplos/missao_teste.mc
    ```


## Como testar os exemplos

Já disponibilizamos missões de teste prontas na pasta exemplos/. Você pode usar elas para verificar o funcionamento ou criar seu proprio arquivo de teste:

-   Arquivos com missao_... no nome: São scripts válidos e funcionam perfeitamente.
-   Arquivos com erro_... no nome: São scripts feitos para falhar propositalmente, acusando os erros de validação do compilador.

## Como executar as missões geradas

Após compilar o arquivo `.mc` e gerar o script python, caso queira testar o script gerado para verificar se está funcionando corretamente, você precisará configurar o ambiente com a biblitoeca MAVSDK para rodá-lo.

Aqui estão os guias para preparação do ambiente e conexão com o simulador (ArduPilot SITL):

* **[Guia de execução para Windows](docs/EXECUCAO_WINDOWS.md)**
* **[Guia de execução para Linux](docs/EXECUCAO_LINUX.md)**

## Equipe

* [Ana Beatriz Soares](https://github.com/alocinny)
* [Danielle Stephany Nunes](https://github.com/Danielle-sn)
* [Michelly Darquia](https://github.com/michellydarquia)
* [Pedro de Melo](https://github.com/pedromonteir1111)

**Orientação:** **Prof. Luis Carlos**
