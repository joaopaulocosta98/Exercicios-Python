termo = int(input('Digite o termo: '))
razão = int(input('Digite a razão: '))
t1 = termo
total = 0
mais = 10
cont = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(t1), end='')
        t1 = t1 + razão
        cont = cont + 1
    mais = int(input('\nQuantos termos a mais você quer? '))
print('Fim')
