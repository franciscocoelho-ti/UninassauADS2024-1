''' Simulando uma competição esportiva, um determinado atleta tem sua nota gerada a partir da média das notas atribuída pelos três jurados. Crie um algoritmo em Python que receba as notas dos jurados e mostre e nota final do atleta. '''

jurado1 = float(input('Nota do primeiro jurado: '))
jurado2 = float(input('Nota do segundo jurado: '))
jurado3 = float(input('Nota do terceiro jurado: '))

notas = (jurado1+jurado2+jurado3)/3

# print(f'Media dos jurados : {notas}')

print('A média das notas foi %.1f' %notas)

