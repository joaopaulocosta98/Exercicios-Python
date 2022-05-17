termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
t1 = termo
cont = 1
while cont <= 10:
    print('{} '.format(t1),end='')
    t1 += razão
    cont += 1
print('Fim!')