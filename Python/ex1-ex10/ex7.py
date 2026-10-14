print ("Mary had a little lamb")
print ("Its fleece was white as %s" % 'snow') # novamente utilizamos uma string dentro de outra string

print(f"Its fleece was white as {'snow'}") # apenas um teste. esse é o modelo utilizado atualmente no python 3 ao envez dos sinais de %

print ("And everywhere that Mary went.")
print ("." * 10) # colocar o * por n faz com que seja printado vezes o N (ex: A * 10 = AAAAAAAAAA)

# criamos variaveis para cada letra na linha abaixo
end1 = "C" 
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end, try removing it to see what happens
print (end1 + end2 + end3 + end4 + end5 + end6, end7 + end8 + end9 + end10 + end11 + end12)

print (end1 , end2 , end3 , end4 , end5 , end6, end7 , end8 , end9 , end10 , end11 , end12) 
# ao trocar os sinais de + por virgulas ele printa dando espaço a cada variavel