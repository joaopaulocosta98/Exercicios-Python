n = int(input('Informe a quantidade termos: '))
t1 = 0
t2 = 1
cont = 3
print('{} → {}'.format(t1,t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' → Fim')