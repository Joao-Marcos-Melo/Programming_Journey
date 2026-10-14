from sys import argv # famoso argv

script, input_file = argv

def print_all(f): # f = file
    print(f.read())

def rewind(f):
    f.seek(0) # a funçao seek volta o cursos para a posição digitada, no caso 0

def print_a_line(line_count, f):
    print(line_count, f.readline()) # aqui ele faz a contagem da linha que esta lendo e le apenas ela

current_file = open(input_file) # cria um nova variavel responsavel por abrir o arquivo de destino

print("First let's print the whole file:\n")

print_all(current_file) # aqui abre e le o conteudo do arquivo

print("Now let's rewind, kind of like a tape.")

rewind(current_file)  # volta o cursor para a posicao zero

print("Let's print three lines:")

current_line = 1   # definimos aqui uma variavel q sera a linha em q estamos no arquivo
print_a_line(current_line, current_file)  # ele printa a primeira linha do arquivo e repete o mesmo nas abaixos

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)