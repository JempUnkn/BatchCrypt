import os
import random
import string

# Nome do arquivo original e do arquivo ofuscado
print("CYJECT - Obfuscador de Scripts Batch")
print()
print("Recomenda-se usar arquivos de Codigo Simples. [For;If;Else] não irão funcionar")
input_filename = input("Digite o nome do arquivo de script original: ")
output_filename = input("Digite o nome do arquivo de script ofuscado: ")

def generate_random_var(length=8):
    """Gera uma string randômica composta apenas de letras."""
    chars = string.ascii_letters  # Removeu os dígitos
    return ''.join(random.choice(chars) for _ in range(length))

# Gera variáveis aleatórias para esconder o comando "set"
header_var1 = generate_random_var()  # Será usada para armazenar "s"
header_var2 = generate_random_var()  # Para "e"
header_var3 = generate_random_var()  # Para "t"

def obfuscate_line(line):
    """Ofusca uma linha do script original, definindo cada caractere em uma variável."""
    definitions = []
    execution = []
    generated_vars = set()  # Para garantir que cada variável seja única na linha
    
    for ch in line:
        var_name = generate_random_var()
        # Garante que não haja conflito com variáveis já usadas, inclusive as do header
        while var_name in generated_vars or var_name in (header_var1, header_var2, header_var3):
            var_name = generate_random_var()
        generated_vars.add(var_name)
        
        # Em vez de usar "set" diretamente, usamos as variáveis do header que representam "s", "e", "t"
        # Assim, a definição fica: %header_var1%%header_var2%%header_var3% "var_name=caractere"
        definitions.append(f'%{header_var1}%%{header_var2}%%{header_var3}% "{var_name}={ch}"')
        execution.append(f"%{var_name}%")
    
    # Retorna as definições (cada uma em uma linha) seguidas da linha de execução que reconstrói o comando
    return "\n".join(definitions) + "\n" + "".join(execution) + "\n"

# Verifica se o arquivo de entrada existe
if not os.path.exists(input_filename):
    print(f"Arquivo '{input_filename}' não encontrado!")
    exit(1)

with open(input_filename, "r", encoding="utf-8") as f:
    original_lines = f.readlines()

# Monta o script ofuscado iniciando com o header
obfuscated_script = "@echo off\n\n"
# Header que define as variáveis que representam o comando "set"
obfuscated_script += f'set "{header_var1}=s"\n'
obfuscated_script += f'set "{header_var2}=e"\n'
obfuscated_script += f'set "{header_var3}=t"\n\n'

# Ofusca cada linha do script original
for line in original_lines:
    line = line.rstrip("\r\n")
    if line:
        obfuscated_script += obfuscate_line(line) + "\n"
    else:
        obfuscated_script += "\n"

# Salva o arquivo ofuscado
with open(output_filename, "w", encoding="utf-8") as f:
    f.write(obfuscated_script)

print(f"Script ofuscado gerado com sucesso: {output_filename}")
