'''
Uma loja que trabalha com crediário funciona da seguinte maneira: se o pagamento ocorre até o
dia do vencimento, o cliente ganha 10% de desconto e é avisado que o pagamento está em dia.
Se o pagamento é realizado até cinco dias após o vencimento o cliente perde o desconto, e se o
pagamento atrasa mais de cinco dias, é cobrada uma multa de 2% por cada dia de atraso. Faça um
programa que lê o dia do vencimento, o dia do pagamento e o valor da prestação e calcule o valor
a ser pago pelo cliente, exibindo as devidas mensagens. suponha que todo vencimento ocorre até
o dia dez de cada mês e os clientes nunca deixam para pagar no mês seguinte.
'''

dia_vencimento = int(input('Informe o dia de vencimento (até dia 10): '))
dia_pagamento = int(input('Informe o dia de pagamento: '))
valor_prestacao = float(input('Informe o valor da prestação: '))

if dia_pagamento <= dia_vencimento:
    valor_prestacao = valor_prestacao - (valor_prestacao * 0.10)
    print('Parabéns, sua prestação está em dias.')
elif dia_pagamento > (dia_vencimento + 5):
    multa = (valor_prestacao * 0.02) * (dia_pagamento - dia_vencimento)
    valor_prestacao = valor_prestacao + multa

# Resultado
print('Valor a Pagar: R$ ', valor_prestacao)


