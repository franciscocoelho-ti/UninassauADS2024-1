'''
 Escreva um algoritmo em Python que leia um caractere do teclado e forneça na tela uma das
 seguintes mensagens:
 
 A -> Alteração
 C -> Consulta
 E -> Exclusão
 I -> Inclusão
 F -> Finalização
 Outro -> Opção Inválida
'''

print('Opções Válidas \nA (Alteração) \nC (Consulta) \nE (Exclusão) \nI (Inclusão) \nF (Finalização) \n ---------')

opcao = input('Informe uma Opção: ')

if opcao == 'A' or opcao == 'a':
    print('Opção Alteração')

elif opcao == 'C' or opcao == 'c':
    print('Opção Consulta')

elif opcao == 'E' or opcao == 'e':
    print('Opção Exclusão')

elif opcao == 'I' or opcao == 'i':
    print('Opção Inclusão')

elif opcao == 'F' or opcao == 'f':
    print('Opção Finalização')

else:
    print('Opção Inválida')
