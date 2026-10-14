# um pequeno pedaço de codigo para testarmos

'''while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i,)  
'''
# esse codigo gera um loop dos caracteres acima, porem esta para o python 2, e estamos utilizando o 3

import time #utilizaremos da funcao time apenas para que possamos ver de um modo melhor os simbulos trocando

while True:
    for i in ["/", "-", "|", "\\"]:
        print(i, end="\r")  # o \r faz com q o cursor volte para o inicio da linha assim reescrevendo
        # Pausa de 0.1 segundos para o olho humano conseguir ver o giro
        time.sleep(0.1)     
