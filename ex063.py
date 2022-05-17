termo = int(input('Digite o Termo: '))
razão = int(input('Dogote a Razão: '))
t1 = termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(t1), end='')
        t1 = t1 + razão
        cont = cont + 1
    mais = int(input('\nQuantas razões você quer mais? '))
print('Fim! {} termos mostrados.'.format(total))


