from sys import argv 

script, filename = argv  # linhas de importacao e definicao de variavel
# a varivel read_text e target sao pra mesma coisa
read_text = open(filename)

print("Here's your %r." % (filename))
print(read_text.read())
read_text.close()

print("-" * 20)

print("We're going to erase %r. " % filename)  # aqui ele cita o nome do arquivo e diz q se quisermos cancelar
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')  # abre o arquivo e o 'w' ja o reescreve apagando tudo

print("Truncating the file. Goodbye!")
target.truncate()   # apaga tudo que esta dentro do arquivo. (mais sobre no caderno) completamente inutil nesse caso

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")  # perguntamos 3 linhas para o usuario para escrevermos no arquivo
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}")
# target.write("{}\n{}\n{}".format(line1, line2, line3)) tambem é possivel fazer desta forma utilizando .format

target.close()  # fecha o arquivo

print("Here's your text: %r." % (filename))
read_text = open(filename)
print(read_text.read())

print("-" * 20)

print("And finally, we close it.")
read_text.close()  # fecha o arquivo