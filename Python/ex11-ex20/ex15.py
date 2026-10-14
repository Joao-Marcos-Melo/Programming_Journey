from sys import argv #importacao 

script,filename=argv # ja temos o arquivo criado 
txt=open(filename)  # digitamos o nome do arquivo para que ele abra
print("Here's your file%r:"%(filename))
print(txt.read())   #primeira vez que vemos a funcao read() 
txt.close()
print("-"*20)
print("Type the filename again:")  
file_again=input(">")
txt_again=open(file_again)
print(txt_again.read())
txt_again.close()