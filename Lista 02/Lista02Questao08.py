'''
Para realizar o cálculo do Imposto de Renda a ser pago, é solicitado a renda anual e o
número de dependentes do contribuinte. A renda líquida é calculada sobre a renda anual
com um desconto de 2% para cada dependente do contribuinte. O contribuinte com uma renda
líquida de até R$ 2.000,00 não paga imposto. Para aqueles que possuem renda líquida entre
R$ 2.000,00 e R$ 5.000,00 o imposto é de 5% sobre o valor da renda líquida; e para rendas
líquidas de R$ 5.000,00 até R$ 10.000,00 é de 10%. Rendas superiores a R$ 10.000,00 pagam
15% de imposto.
'''

renda_anual = float(input('Informe sua renda anual: '))
num_dependentes = int(input('Informe o número de dependentes: '))

renda_liquida = renda_anual - (renda_anual / 100 * num_dependentes)
valor_imposto = 0

if renda_liquida < 2000:
    print('Você não paga imposto')
elif renda_liquida >= 2000 and renda_liquida < 5000:
    imposto = valor_imposto * 0.05
elif renda_liquida >= 5000 and renda_liquida < 10000:
    imposto = valor_imposto * 0.10
elif renda_liquida >= 10000:
    imposto = valor_imposto * 0.15

print('Valor a pagar de imposto: ', imposto)



