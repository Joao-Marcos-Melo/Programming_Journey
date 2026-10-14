from sys import argv # Aqui vemos sobre sys e argv, sys é um modulo padrao do python 

script, dados = argv #ele funciona ao digitarmos para executar o script sendo necessario definir as variaveis nessa hora tambem

print("Loading script: ", script)
print("Loading ", dados)
print("..." * 10)

name = input("What's your name? ") # aqui juntei com o input() 
age = input("How old are you? ")

print(f"Your name is {name} and you have {age} years old.")