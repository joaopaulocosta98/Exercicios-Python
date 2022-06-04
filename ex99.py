from time import sleep
def maior(* m):
    contador = 0
    maior = 0
    print(f'Os números listados foram...')
    for valor in m:
        print(f'{valor}',end=' ')
        sleep(0.5)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1

    print(f'\nForam listados {contador} números')
    print(f'E o maior número listado foi {maior}')
    print('-='*20)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()