'''
Uma cidade classifica um índice de poluição menor que 35 como agradável; de 35 até 60
desagradável e acima de 60 perigoso. Escreva um algoritmo em Python que leia um número
real representando o índice de poluição e imprime a classificação adequada para ele.
'''

indice = float(input('Informe o índice: '))

if indice < 35:
    print('Classificação Agradável')
elif indice >= 35 and indice <= 60:
    print('Classificação Desagradável')
else:
    print('Classificação Perigosa')

