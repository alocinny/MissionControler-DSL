import sys
import os
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


    if parser.getNumberOfSyntaxErrors() > 0: # Se houver erros de sintaxe, aborta
        print(f"Abortando: Encontrados {parser.getNumberOfSyntaxErrors()} erros de sintaxe.")
        return

    # 2. Semântica (Visitor)
    print(">>> Analisando Semântica...")
    visitor = MissionCompiler()
    try:
        visitor.visit(tree)
    except Exception as e:
        print(f"ERRO SEMÂNTICO: {e}")
        return

    # 3. Backend (Geração de Código)
    print(">>> Gerando Código Python...")
    generator = MissionCodeGenerator(visitor.ir)
    codigo_final = generator.generate()

    # 4. Salvar Arquivo
    output_dir = "build"
    os.makedirs(output_dir, exist_ok=True)
    
    file_name_with_ext = os.path.basename(input_file)
    
    # Separa o nome do arquivo base da extensão ('.mc')
    base_name, _ = os.path.splitext(file_name_with_ext)
    
    # Constrói o novo nome do arquivo com a extensão .py
    output_filename = f"{base_name}.py"
    output_file = os.path.join(output_dir, output_filename)
    
    with open(output_file, "w", encoding='utf-8') as f:
        f.write(codigo_final)
    
    print(f"Sucesso! Arquivo '{output_file}' gerado.")
    print(f"Para rodar: python {output_file}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_missao.mc>")
    else:
        main(sys.argv[1])