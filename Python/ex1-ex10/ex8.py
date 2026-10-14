formatter = "%r %r %r %r" # utilizamos aqui o %r como placeholder
# caso queiramos fazer com f-strings mudamos de "%r %r %r %r" para "{!r} {!r} {!r} {!r}" e adicionamos um .format no lugar do % nas linhas abaixo

print(formatter % (1, 2, 3, 4))  #a saida nao utilizara aspas pois a representacao bruta de um numero é ele mesmo
print(formatter % ("one", "two", "three", "four")) # a saida ficara com aspas simples 
print(formatter % (True, False, False, True)) # mesma coisa dos numeros, booleano sai como ele mesmo
print(formatter % (formatter, formatter, formatter, formatter)) # aqui a variavel que criamos guarda o texto puro, e quando printamos ele dessa forma estamos injetando o texto da variavel direto
print(formatter % (
    "I had this thing.",
    "That you could type up right.", 
    "But it didn't sing.",  # essa linha é a unica que contem aspas duplas na saida, isso acontece pois o nosso texto ja possui aspas simples
    "So I said goodnight."
    ))

print("-" * 20)

#exemplo utilizando f-strings

formatter = "{!r}, {!r}, {!r}, {!r}" # note que nas linhas abaixo ele imprimira inclusive as virgulas

print(formatter.format (1, 2, 3, 4))  
print(formatter.format ("one", "two", "three", "four"))
print(formatter.format (True, False, False, True))
print(formatter.format (formatter, formatter, formatter, formatter))
print(formatter.format (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.", 
    "So I said goodnight."
    ))