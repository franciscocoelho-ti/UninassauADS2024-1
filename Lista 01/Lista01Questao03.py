''' Crie um algoritmo em Python para ajudar um vendedor de mercadorias. O algoritmo deve receber do vendedor o valor de compra da mercadoria, e a porcentagem de lucro que ele deseja adquirir sobre a mercadoria. Ao final mostre o valor de venda do produto. '''


valor_compra = float(input('Informe o valor da mercadoria: '))
porcentagem = float(input('Informe a porcentagem do lucro: '))

lucro = (valor_compra / 100) * porcentagem
valor_venda = valor_compra + lucro

print('O valor de venda é: ', valor_venda)
print('O lucro do vendedor será de: ', lucro)

