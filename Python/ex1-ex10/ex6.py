x = "there are %d types of people." % 10 # aqui eu crio uma variavel e dou a ela o valor 10 utilizando do %d
binary = "binary" #string
do_not = "don't" # string
y = "Those who know %s and those who %s" % (binary, do_not) # aqui eu faço o mesmo porem adiciono duas strings dentro de uma utilizando os %s 
#primeira string = Those who know %s and those who %s" (outras 2 strings que estou adicionando = binary, do_not)

print(x)
print(y)

print("I said: %r." % x) #aqui a string vem do uso do %r pois ele puxa as aspas originais do texto
print("I also said: '%s'." % y) # aqui a string vem do uso das ' utilizadas dentro de uma string que ja possui "

hilarius = False
joke_evaluation = "Isn't that joke so funny?! %r" # nessa parte nao entra como uma string adicional pois a variavel hilarius é um booleano (verdadeiro ou falso)
#nota: aqui estamos utilizando o %r dentro da variavel como um molde e ao executalo no print abaixo o % diz algo como "pegue o valor de hilarius e encaixe onde esta o %r"
print(joke_evaluation % hilarius) 

w = "This is the left side of..."
e = "a string with a right side."

print(w + e) #utilizamos aqui o sinal de + para que ele una as 2 strings em uma nova gerando assim uma string mais longa