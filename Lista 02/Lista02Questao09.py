'''
Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente. A tabela de preços do hospital é a seguinte:

 Quartos:
 - particular: R$ 125,00
 - conjunto: R$ 95,00
 - enfermaria: R$ 75,00

 Serviços:
 Telefone: R$ 1,75
 Televisão: R$ 3,50

 Descontos:
 - Total superior à R$ 1.000,00: 15%
 - Total superior à R$ 500,00: 10%
 - Total inferior à R$ 500,00: 5%

 Escreva um algoritmo em Python que leia o número de dias gastos no hospital, um caractere representando o tipo de quarto utilizado (P, C ou E), um caractere indicando se usou ou não o telefone (S ou N), um caractere indicando se usou ou não a televisão (S ou N) e produza a seguinte saída:
 
 Hospital Exemplo S/A
 Diárias : 5
 Tipo quarto : PARTICULAR
 Diárias : R$ 625,00
 Telefone : R$ 0,00
 Televisão : R$ 3,50
 Total : R$ 628,50
 Descontos : R$ 62,85
 Valor pago : R$ 565,65
'''


quant_dias = int(input('Informe a quant. de dias: '))
tipo_quarto = input('Informe o tipo de quarto (P, C ou E): ')
uso_telefone = input('Houve uso do Telefone (S ou N): ')
uso_televisao = input('Houve uso da Televisão (S ou N): ')
valor_total = 0

# Resultados
print('-' * 20)
print('Hospital Exemplo S/A')
print(f'Diárias: {quant_dias}')

# Verificar gasto com o quarto
if tipo_quarto == 'P' or tipo_quarto == 'p':
    valor_total = valor_total + (quant_dias * 125)    
    # Resultados
    print('Tipo quarto: PARTICULAR')
    print(f'Diárias : R$ {quant_dias * 125}')

elif tipo_quarto == 'C' or tipo_quarto == 'c':
    valor_total = valor_total + (quant_dias * 95)
    # Resultados
    print('Tipo quarto: Conjunto')
    print(f'Diárias : R$ {quant_dias * 95}')

elif tipo_quarto == 'E' or tipo_quarto == 'e':
    valor_total = valor_total + (quant_dias * 75)
    # Resultados
    print('Tipo quarto: Enfermaria')
    print(f'Diárias : R$ {quant_dias * 75}')


# Verificar gasto com a Televisao
if uso_televisao == 'S' or uso_televisao == 's':
    valor_total = valor_total + 3.50
    # Resultados
    print('Televisão : R$ 3,50')
else:
    # Resultados
    print('Televisão : R$ 0,00')

d
# Verificar gasto com o Telefone
if uso_telefone == 'S' or uso_telefone == 's':
    valor_total = valor_total + 1.75
    # Resultados
    print('Telefone : R$ 1,75')
else:
    # Resultados
    print('Telefone : R$ 0,00')

# Resultados
print(f'Total : R$ {valor_total}')


# Verificar o Desconto
if valor_total >= 1000: # 15%
    desconto = valor_total * 0.15
    valor_total = valor_total - desconto
    # Resultados
    print(f'Desconto: {desconto}')
elif valor_total >= 500 and valor_total < 1000:
    desconto = valor_total * 0.10
    valor_total = valor_total - desconto
    # Resultados
    print(f'Desconto: {desconto}')
else:
    desconto = valor_total * 0.05
    valor_total = valor_total - desconto
    # Resultados
    print(f'Desconto: {desconto}')

# Resultados
print(f'Valor pago : R$ {valor_total}')








