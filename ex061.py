from math import factorial
n1 = int(input('Informe o valor para calcular o se faltorial: '))
c = n1
fac = factorial(n1)
print('Calculando {}! = '.format(n1),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(fac),end='')
    c -= 1

