'''
Escreva um algoritmo Python que leia uma sequência de números inteiros terminada por –1 e imprima na tela a soma e a média aritmética destes números.

Obs: o valor –1 é somente um terminador e não deve ser considerado nos cálculos.
'''
quant = 0
num = 0
soma = 0

while num != -1:
    soma += num
    num = int(input("Informe um número inteiro:"))
    if num != -1:
        quant += 1
media = soma/quant

print(f"A soma dos números é: {soma}\nA média dos números é: {media}") #imprima na tela a soma e a média aritmética destes números.