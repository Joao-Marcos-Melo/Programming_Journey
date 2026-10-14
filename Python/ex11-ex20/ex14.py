from sys import argv # esse codigo faz basicamente o que o exercicio 12 pedia, unir from sys import argv com input()

script, user_name, date = argv # definimos as variaveis direto ao chamar o script
prompt = 'Don\'t lie... ' # estamos usando aspas simples aqui, portanto as aspas dentro do texto devem vir com \ antes

print("Hi %s, I'm the %s script." % (user_name, script)) # novamente para nos lembrar %s = strings
print("%s" % (date))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % (user_name))
likes = input(prompt)

print("Where do you live %s?" % (user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)) # %r = representacao real (bruta)