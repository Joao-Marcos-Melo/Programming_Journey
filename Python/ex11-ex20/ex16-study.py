import os  # Importamos o 'os' apenas para apagar os arquivos de teste no final do script

nome_arquivo = "arquivo_de_teste.txt"
nome_backup = "backup_binario.bin"

print("=== 1. TESTANDO O MODO 'x' (Criação Exclusiva) ===")
# O modo 'x' cria o arquivo, mas se ele já existir, o Python dá erro para proteger dados antigos.
# Vamos usar o 'try/except' só para o caso de você rodar o script duas vezes seguidas.
try:
    arquivo_x = open(nome_arquivo, "x")
    arquivo_x.write("Linha 1: Arquivo criado com sucesso pelo modo 'x'!\n")
    arquivo_x.close()
    print(f"[{nome_arquivo}] criado com segurança!")
except FileExistsError:
    print(
        f"Atenção: O arquivo [{nome_arquivo}] já existia. O modo 'x' evitou que ele fosse apagado."
    )

print("-" * 40)

print("=== 2. TESTANDO O MODO 'r' (Leitura Pura) ===")
# O modo 'r' é o padrão. Apenas lê o conteúdo e dá erro se tentarmos usar .write()
arquivo_r = open(nome_arquivo, "r")
conteudo = arquivo_r.read()
print("Conteúdo lido pelo modo 'r':")
print(conteudo)
arquivo_r.close()

print("-" * 40)

print("=== 3. TESTANDO O MODO 'a' (Append / Anexar) ===")
# O modo 'a' abre o arquivo e coloca o cursor lá no final. Ele NÃO apaga o que já estava lá.
arquivo_a = open(nome_arquivo, "a")
arquivo_a.write(
    "Linha 2: Esta linha foi adicionada ao final pelo modo 'a' sem apagar nada!\n"
)
arquivo_a.close()

# Vamos abrir em modo 'r' rapidinho só para provar que a primeira linha não sumiu
arquivo_teste = open(nome_arquivo, "r")
print("Como o arquivo ficou após o modo 'a':")
print(arquivo_teste.read())
arquivo_teste.close()

print("-" * 40)

print("=== 4. TESTANDO O MODO 'r+' (Leitura e Escrita ao mesmo tempo) ===")
# O modo 'r+' permite ler o arquivo e depois escrever nele, sem apagar tudo no momento de abrir.
arquivo_r_mais = open(nome_arquivo, "r+")

print("Lendo os primeiros 15 caracteres no modo 'r+':")
print(arquivo_r_mais.read(15))  # Lê apenas os 15 primeiros caracteres

# Como o cursor parou no 15º caractere, se usarmos .write() agora, ele vai sobrescrever o texto a partir dali!
# Para evitar estragar o meio do texto, vamos mandar o cursor para o final do arquivo usando o .seek(0, 2)
# Ou podíamos mandar para o começo com .seek(0). Vamos mandar para o final:
arquivo_r_mais.seek(0, 2)
arquivo_r_mais.write(
    "Linha 3: Adicionada usando o modo misto 'r+'!\n"
)
arquivo_r_mais.close()

print("-" * 40)

print("=== 5. TESTANDO O MODO 'rb' e 'wb' (Binário) ===")
# Arquivos binários não lidam com texto formadinho (strings), mas sim com "bytes" crus do sistema.
# Vamos abrir nosso arquivo de texto como binário ('rb') e copiar para um novo arquivo ('wb').
arquivo_rb = open(nome_arquivo, "rb")
dados_binarios = arquivo_rb.read()
arquivo_rb.close()

print(f"Assim é como o computador vê nosso arquivo por baixo dos panos (bytes):")
print(dados_binarios[:40])  # Imprimindo apenas um pedacinho dos bytes

arquivo_wb = open(nome_backup, "wb")
arquivo_wb.write(dados_binarios)
arquivo_wb.close()
print(f"Cópia exata salva como [{nome_backup}] usando o modo 'wb'.")

print("-" * 40)

print("=== 6. TESTANDO O MODO 'w' (Write / Sobrescrever) ===")
print("Atenção! Agora vamos abrir o arquivo original com o modo 'w'.")
input("Pressione ENTER para ver o poder destrutivo do modo 'w'...")

# Abrir com 'w' apaga TODO o conteúdo imediatamente!
arquivo_w = open(nome_arquivo, "w")
arquivo_w.write(
    "Tudo o que existia antes foi apagado. Sobrou apenas esta frase do modo 'w'."
)
arquivo_w.close()

# Lendo pela última vez para confirmar a destruição
arquivo_final = open(nome_arquivo, "r")
print("\nResultado final do arquivo após o modo 'w':")
print(arquivo_final.read())
arquivo_final.close()

print("-" * 40)

# FAXINA: Perguntamos se você quer apagar os arquivos criados para manter seu computador limpo
limpar = input("Deseja deletar os arquivos de teste criados no seu computador? (s/n): ")
if limpar.lower() == "s":
    os.remove(nome_arquivo)
    os.remove(nome_backup)
    print("Arquivos de teste removidos com sucesso. Estudo concluído!")
else:
    print(f"Arquivos mantidos! Você pode abrir [{nome_arquivo}] no seu Bloco de Notas para ver.")