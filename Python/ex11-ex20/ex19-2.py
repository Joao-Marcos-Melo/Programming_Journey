from sys import argv

arg_fruta, arg_leite, arg_vitamina = argv

# func
def batido(fruta, liquido, resultado):
    print(f"Se eu bater {fruta} com {liquido} vira: {resultado}\n")

# call 1
batido("Maçã", "Água", "Suco de maçã")

# call 2 
fruta_bater = "Mamão"
liquido_bater = "Leite"
resultado_bater = "Vitamina de mamão"

batido(fruta_bater, liquido_bater, resultado_bater)

# call 3
batido(10 + 5, 10 - 5, 20)

# call 4
fruta_escolhida = input("Escolha uma fruta para fazer suco:")
agua = "água"

suco_fruta = "suco de " + fruta_escolhida

batido(fruta_escolhida, agua, suco_fruta)

# call 5
batido(arg_fruta, arg_leite, arg_vitamina)

# call 6
fruta_numerica = 8
liquido_numerico = 3
resultado_numerico = fruta_numerica + liquido_numerico
batido(fruta_numerica + 3, liquido_numerico + 1, resultado_numerico)

# call 7
fruta_escolhida_outra = input("Escolha uma fruta para fazer suco:")
junçao_batido = "vitamina de ", fruta_escolhida_outra 
batido(fruta_escolhida_outra, arg_leite, junçao_batido)

# call 8
num = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
result = num + num2 / 4 * 8
result2 = num - num2 * 4 / 8 
catastrofe = result + result2

batido(result, result2, catastrofe)

# call 9

# call 10