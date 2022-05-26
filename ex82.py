lista = []
opção = 'S'
pares = []
ímpares = []
while opção:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            ímpares.append(n)
    else:
        print('Valor duplicado!')
    opção = str(input(('Deseja continuar?[S/N] '))).strip().upper()
    print('-*'*20)

    if opção == 'N':
        break
print(f'Foram digitados os valores {lista}.')
print(f'Os números pares são {pares}.')
print(f'Os números ímpares são {ímpares}.')
