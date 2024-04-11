'''
Escreva um algoritmo em Python que leia dois valores inteiros e apresente o maior dos valores
lidos, ou se os números são iguais.
'''

numero1 = int(input('Informe o 1º valor: '))
numero2 = int(input('Informe o 2º valor: '))

if numero1 > numero2:
    # print('Número1 é o maior')
    print(f'{numero1} é maior que {numero2}')
elif numero2 > numero1:
    # print('Número2 é o maior')
    print(f'{numero2} é maior que {numero1}')
else:
    print(f'Foi informado {numero1} nas duas entrada de dados')


