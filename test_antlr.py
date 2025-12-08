import sys
from antlr4 import *
from generated.compiler.MissionControlLexer import MissionControlLexer
from generated.compiler.MissionControlParser import MissionControlParser

dsl_code = """
mission "Teste ANTLR" {
    settings {
        max_altitude: 30.0
        base_speed: 6.0
    }
    waypoints {
        "Home": -27.6, -48.5
    }
    start {
        takeoff(10.0)
    }
    task "Missao 1" {
        goto("Home")
    }
    end {
        land()
    }
}
"""

def main():
    print("testando parser")
    input_stream = InputStream(dsl_code)
    
    # lexer (transforma texto em tokens)
    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # parser (transforma tokens em arvore)
    parser = MissionControlParser(stream)
    
    # iniciar pela regra raiz
    tree = parser.prog()
    
    # final
    print("arvore Sintática gerada:")
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main()