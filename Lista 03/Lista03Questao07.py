'''
Escreva um algoritmo em Python que gere, para um valor n (maior igual a zero) fornecido pelo usuário, um "quadrado" de n linhas e n colunas que tenha caracteres '*' nas posições da diagonal principal e os caracteres '.' nas demais posições. Por exemplo, para n = 5 o programa deve gerar:

  * - - - -
  - * - - -
  - - * - -
  - - - * -
  - - - - *
'''


numero = int(input('Informe o valor de N: '))

for linha in range(numero):
  print('')
  for coluna in range(numero):
    if linha == coluna: 
      print('* ', end = '')
    else:
      print('- ', end = '')


