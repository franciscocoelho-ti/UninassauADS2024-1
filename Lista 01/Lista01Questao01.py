''' Escreva um algoritmo em Python que receba de um usuário a altura de um determinado andar de um prédio, e quantos andares o prédio possui. Ao final mostre a altura total do prédio. '''

# Entrada
altura = float(input("Informe a altura do andar: "))
quantidade_andares = int(input("Informe quantos andares tem o prédio: "))

# Processamento
altura_total=(altura * quantidade_andares)

# Saída
print(f"A altura total do prédio é: {altura_total}")



