from random import randint
from time import sleep
números = []
def sorteia():
    print('Sorteando...')
    sleep(0.4)
    for c in range(0,5):
        n = randint(1,10)
        números.append(n)
        print(f'{n}',end=' ')
        sleep(0.3)


def somaPar(lista):
    sleep(0.4)
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'\nSomando os valores pares entre {lista}, temos {soma}')



sorteia()
somaPar(números)

