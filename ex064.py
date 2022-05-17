print('-=-'*20)
print('Seguencia de Fibonacci')
print('-=-'*20)
n = int(input('Digite a quantidade de termos: '))
t1 = 0
t2 = 1
cont = 3
print('{} - {} '.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' - {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - Fim!')

