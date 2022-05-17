n = 0
total = 0
cont = 0
while n != 999:
    n = int(input('Digite o número inteiro: '))
    if n != 999:
        total = total + n
        cont = cont + 1
    elif n == 999:
        print('Fim, com {} digitados que somados da {}'.format(cont, total))