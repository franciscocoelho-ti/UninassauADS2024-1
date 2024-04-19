'''
Escreva um algoritmo em Python que leia um inteiro N e imprime a soma dos N primeiros números
inteiros positivos.
'''

# Como não sabemos o valor de N, fizemos o input para receber o valor do usuário.
# O contador começa com valor 1 por ser o primero valor inteiro positivo
# A soma inicia com zero por ser um valor neutro, não interferindo no valor final
numero_n = int(input('Informe o valor de N: '))
contador = 1  
soma = 0 

# A repetição (while) ficará em execução até que o valor do contador ultrapasse o valor de N, enquanto
# ele o contador estiver menor ou igual a repetição continuará.
while contador <= numero_n:

    # A cada repetição a soma recebe o valor da própria variável soma, mais o valor da variável contador
    # A cada repetição o contador receber o valor da variável contador, mais o valor 1
    # soma += contador, o mesmo que "soma = soma + contador"
    # contador += 1, o mesmo que "contador = contador + 1"
    soma += contador 
    contador += 1

# Ao final exibe-se o valor da variável soma.
print('A soma foi', soma)

