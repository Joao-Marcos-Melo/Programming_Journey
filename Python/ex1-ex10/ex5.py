name = 'Joao Marcos'
age = 18
height_cm = 185 #cm
height_inches = height_cm / 2.54 
weight_kg = 68 #kg
weight_pounds = weight_kg / 0.453592
eyes = 'black'
teeth = 'white'
hair = 'dark_brown'
text = 'alberto\n' #variavel para teste do %r

print ("Let's talk about %s" % name)  # %s para strings
print ("He's %d centimeters tall and %d in inches" % (height_cm, height_inches)) # %d para numeros inteiros (decimais)
print ("He's %d kilos heavy and %d in pounds" % (weight_kg, weight_pounds))
print ("Actually that's not too heavy")
print ("He's got %s eyes and %s hair" % (eyes, hair))
print ("His teeth are usually %s depending on the coffee" % teeth)

#this line is tricky, try to get it exactly right
print ("(cm/kg) If I add %d, %d, and %d I get %d or %d (in inches/pounds)" % (age, height_cm, weight_kg, age + height_cm + weight_kg, age + height_inches + weight_pounds))

#teste com %r

print ("-" * 20) #para uma divisao de linha

print ("com %%r: %r" % weight_pounds)

#teste com funcao round()
print("sem arredondar usando %%f: %f" % weight_pounds)
print("sem arredondar chamando a variavel:", weight_pounds)
print ("Arrendondando usando a função round()", round(weight_pounds)) # %f usado para floating numbers, ou numeros quebrados