import sys
import os
from antlr4 import *
from MissionControlLexer import *
from MissionControlParser import *
from analisador_semantico import analise
from compilador import gera_codigo

def main():
    if len(sys.argv) < 2:
        print("uso: python main.py <arquivo.mc>")
        return

    input_file = sys.argv[1]
    input_stream = FileStream(input_file, encoding='utf-8')

    lexer = MissionControlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MissionControlParser(stream)
    
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("erro de sintaxe encontrado. Abortando.")
        return

    try:
        analise(tree)
    except Exception as e:
        print(f"{e}")
        return
    
    original_stdout = sys.stdout

    output_dir = 'missoes_geradas'
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.basename(input_file)
    output_filename = base_name.replace('.mc', '.py')
    output_path = os.path.join(output_dir, output_filename)
    
    with open(output_path, 'w') as f:
        sys.stdout = f
        gera_codigo(tree)
    
    sys.stdout = original_stdout
    
    print(f"arquivo gerado: {output_path}")

if __name__ == '__main__':
    main()