opção = 'S'
lista = []
dado = []
maispesadas = 0
maisleves = 0
while opção:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))
    if len(lista) == 0:
        maispesadas = maisleves = dado[1]
    else:
        if dado[1] > maispesadas:#para descobrir o maior peso
            maispesadas = dado[1]
        if dado[1] < maisleves:#para descobrir o menor peso
            maisleves = dado[1]
    lista.append(dado[:])
    dado.clear()
    opção = str(input('Deseja continuar?[S/N]')).strip().upper()
    print('-='*20)
    if opção == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas!')
print(f'O maior peso foi de {maispesadas}Kg, ',end='')
for p in lista:
    if p[1] == maispesadas:
        print(f'{p[0]}...')
print(f'\nO menor peso foi de {maisleves}Kg, ',end='')
for p in lista:
    if p[1] == maisleves:
        print(f'{p[0]}...')


