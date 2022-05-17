soma = 0
for cn in range(1, 7):
    num = int(input('Digite {}º valor: '.format(cn)))
    if num % 2 == 0:
        soma = soma + num
print('A soma dos valores pares é {}'.format(soma))
