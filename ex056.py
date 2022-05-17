maiores = 0
menores = 0
for c in range(1, 6):
    peso = float(input('Informe o seu peso: '))
    if c == 1:
        maiores = peso
        menores = peso
    else:
        if peso > maiores:
            maiores = peso
        if peso < menores:
            menores = peso
print('O maior peso lido foi {:.1f}kg'.format(maiores))
print('O menor peso lido foi {:.1f}kg'.format(menores))
