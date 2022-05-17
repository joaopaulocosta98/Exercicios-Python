from datetime import date
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite a data de nascimento: '))
    idade = date.today().year - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('O total de pessoas maiores de idade são {}'.format(totalmaior))
print('O total de pessoas menores de idade são {}'.format(totalmenor))
