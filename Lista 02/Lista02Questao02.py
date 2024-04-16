'''
Escreva um algoritmo em Python que leia um número real fornecidos pelo usuário e calcule sua raiz quadrada. O programa deve evitar calcular a raiz de um número negativo.
'''

from math import sqrt

numero = float(input('Informe um valor: '))
    
if numero > 0:
    resultado = sqrt(numero)
    print(f'A raiz quadrada de {numero} é {resultado}')
else:
    print('Informe um número maior que zero!')
    










