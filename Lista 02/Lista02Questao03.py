'''
Escreva um algoritmo em Python que leia 4 valores: P, A, B e C. Se P=1 então calcular a média aritmética de A, B e C e escrever esta média; se P = 2 somar os 3 valores atribuindo este valor a uma variável qualquer e escrevendo esta soma; se P = 3 fazer um teste para saber se B é par, se é par escrever a mensagem e o valor, caso contrário escrever que é ímpar.
Se for qualquer outro valor mostrar a mensagem “operação inválida”.
'''

p = int(input('Informe o valor de P: '))
a = int(input('Informe o valor de A: '))
b = int(input('Informe o valor de B: '))
c = int(input('Informe o valor de C: '))

if p == 1:
    media = (a + b + c) / 3
    print(f'A média foi {media}')
elif p == 2:
    soma = a + b + c
    print('A soma foi ', soma)
elif p == 3:
    if b % 2 == 0:
        print('O valor de B é par')
    else:
        print('O valor de B é impar')
else:
    print('Opção inválida')


