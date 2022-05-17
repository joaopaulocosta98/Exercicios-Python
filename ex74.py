from random import randint
lista =(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
print('Os números sorteados são: ',end='')
for n in lista:
    print(f'{n}',end=' ')
print(f'\nO maior número sorteado foi: {max(lista)}')
print(f'O menor número sorteado foi: {min(lista)}')