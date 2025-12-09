import sys
from antlr4 import *
from generated.compiler.MissionControlLexer import MissionControlLexer
from generated.compiler.MissionControlParser import MissionControlParser
from compiler.visitor import MissionCompiler 
from generator import MissionCodeGenerator

def main(input_file):
    # 1. Frontend (ANTLR)
    input_stream = FileStream(input_file, encoding='utf-8')
    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MissionControlParser(stream)
    tree = parser.missionBlock()

    # 2. Semântica (Visitor)
    print(">>> Analisando Semântica...")
    visitor = MissionCompiler()
    try:
        visitor.visit(tree)
    except Exception as e:
        print(f"❌ ERRO SEMÂNTICO: {e}")
        return

    # 3. Backend (Geração de Código)
    print(">>> Gerando Código Python...")
    generator = MissionCodeGenerator(visitor.ir)
    codigo_final = generator.generate()

    # 4. Salvar Arquivo
    output_file = "mission_runner1.py"
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(codigo_final)
    
    print(f"✅ Sucesso! Arquivo '{output_file}' gerado.")
    print(f"🚀 Para rodar: python {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_missao.mc>")
    else:
        main(sys.argv[1])