'''
print("How old are you?"),  #as virgulas no python 3 ja nao servem para nada utilizamos de end="" para fazer a funcao delas
age = input()
print("How tall are you?"),
height = input()
print("How much do you weight?"),
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))


print("-" * 20)
'''
#codigo atualizado utilizando as f-strings e os end

print("How old are you?", end =" ") # a funcao do end="" é para que o print continue na mesma linha e nao desca para uma debaixo.
age = input()
print("How tall are you?", end =" ")
height = input()
print("How much do you weight?", end =" ")
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

""" tambem é possivel fazer sem o uso dos prints iniciais pois o input ja tem essa funcao de print (NOTA: vi agora q esse é o proximo exercicio)

age = input(How old are you?)
height = input(How tall are you?)
weight = input(How much do you weight?)

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

"""