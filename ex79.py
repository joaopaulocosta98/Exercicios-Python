from time import sleep
opção = "S"
num = list()
while opção == 'S':
    n = int(input("Digite um Valor: "))
    if n in num:
        print('Valor duplicado!Não adicionado...')
    else:
        print('Adicionando número', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.')
        sleep(0.4)
        num.append(n)
        print('Valor adicionado!')
    opção = input('\nDeseja continuar?[S/N] ').strip().upper()
    print('-=' * 20)
    if opção == 'N':
        break
num.sort()
print(f'Os valores informados foram {num}')