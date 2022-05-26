num = 0
total = []
pares = []
impar = []
for c in range(0,7):
    num = int(input(f'Digite {c + 1}o número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)
    total.append(num)
total.sort()
print(f'Foram digitados os números {total}')
pares.sort()
print(f'Os números pares são {pares}.')
impar.sort()
print(f'Os números ímpares são {impar}.')

