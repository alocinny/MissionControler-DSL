from antlr4 import *
from generated.compiler.MissionControlLexer import MissionControlLexer
from generated.compiler.MissionControlParser import MissionControlParser
from compiler.visitor import MissionCompiler

# bateria Inválida (tem que falhar)
codigo_invalido = """
mission "Teste Falha" {
    settings {
        max_altitude: 30.0
        failsafe_battery: 5  # ERRO! Mínimo é 10
    }
    waypoints { "Home": 0.0, 0.0 }
    start { takeoff(10) }
    end { land() }
}
"""

print("\nvalidando regra de bateria")
try:
    input_stream = InputStream(codigo_invalido)
    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MissionControlParser(stream)
    tree = parser.prog()

    visitor = MissionCompiler()
    visitor.visit(tree)
    print("o compilador deveria ter falhado, mas aceitou")
except Exception as e:
    print(f"o compilador pegou o erro: {e}")

# código Válido (tem que extrair dados)
codigo_valido = """
mission "Missao Real" {
    settings {
        failsafe_battery: 25
        base_speed: 15.0
    }
    waypoints {
        "Ponto A": -23.5, -46.6, 10.0
        "Ponto B": -23.6, -46.7
    }
    start { takeoff(10) }
    end { land() }
}
"""

print("\nextração de dados")
try:
    input_stream = InputStream(codigo_valido)
    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MissionControlParser(stream)
    tree = parser.prog()

    visitor = MissionCompiler()
    visitor.visit(tree)
    
    print("dados extraídos (IR):")
    print(visitor.ir["settings"])
    print(visitor.ir["waypoints"])
    
except Exception as e:
    print(f"ERRO: {e}")

# missão completa com validação de aypoint
print("\nmissão Completa")
codigo_full = """
mission "Operação SAE" {
    settings { max_altitude: 50.0 }
    waypoints { 
        "Alpha": -23.5, -46.6, 20.0 
    }
    start { 
        takeoff(15) 
    }
    task "Ronda" {
        goto("Alpha")
        hover(5)
    }
    end { 
        rtl() 
    }
}
"""

try:
    input_stream = InputStream(codigo_full)
    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MissionControlParser(stream)
    tree = parser.prog()

    visitor = MissionCompiler()
    visitor.visit(tree)
    
    print("comandos Gerados:")
    for cmd in visitor.ir["commands"]:
        print(cmd)

except Exception as e:
    print(f"ERRO: {e}")

# takeoff no lugar errado (tem que falhar)
print("\nvalidando Ccntexto do takeoff")
codigo_ilegal = """
mission "Decolagem Ilegal" {
    settings { max_altitude: 50.0 }
    waypoints { "Home": 0.0, 0.0 }
    start { speed(5) }
    task "Perigo" {
        takeoff(10) # ERRO! Não pode decolar no meio de uma task
    }
    end { land() }
}
"""
try:
    input_stream = InputStream(codigo_ilegal)
    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MissionControlParser(stream)
    tree = parser.prog()

    visitor = MissionCompiler()
    visitor.visit(tree)
    print("o compilador deixou decolar dentro de uma task")
except Exception as e:
    print(f"bloqueou takeoff ilegal: {e}")