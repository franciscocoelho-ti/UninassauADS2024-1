# -------------------------------------------
# Código Desenvolvido pela aluna Ana Caroline
# -------------------------------------------


valor_compra = float(input('Informe o valor da mercadoria: '))
porcentagem = float(input('Informe a porcentagem de lucro: '))

valor = (porcentagem/100)*valor_compra
venda = (valor+valor_compra)

print('O valor de venda é: ',venda)
print('O lucro do vendedor será de: ',valor)
