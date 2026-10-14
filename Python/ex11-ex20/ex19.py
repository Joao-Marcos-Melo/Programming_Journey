def cheese_and_crackers(cheese_count, boxes_of_crackers): # criamos a funcao
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers") 
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:") 
cheese_and_crackers(20, 30)  # chamamos a funcao aqui apenas e passamos os valores delas 

print("OR, we can use variables from our script:") # podemos criar variaveis fora da funcao e depois passalas para dentro
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # aqui chamamos a funcao e passamos as variaveis

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # podemos colocar matematica na funcao tambem 

print("And we can combine the two, variables and math:")  # por fim podemos tambem combinar as variaveis e matematica
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)