cont = 0
soma = 0
for num in range (1, 501, 2):
    if num % 3 == 0:
        cont = cont + 1
        soma = soma + num
print('A soma de todos os {} números ímpares e multiplos de 3 é {}'.format(cont,soma))
