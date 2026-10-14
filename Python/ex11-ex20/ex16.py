from sys import argv 

script, filename = argv  # linhas de importacao e definicao de variavel

print("We're going to erase %r. " % filename)  # aqui ele cita o nome do arquivo e diz q se quisermos cancelar
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')  # abre o arquivo e o 'w' ja o reescreve apagando tudo

print("Truncating the file. Goodbye!")
target.truncate()   # apaga tudo que esta dentro do arquivo. (mais sobre no caderno)

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")  # perguntamos 3 linhas para o usuario para escrevermos no arquivo
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)  # escrevemos dentro do arquivo
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()  # fecha o arquivo