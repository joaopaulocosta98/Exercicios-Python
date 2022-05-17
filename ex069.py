import random
nj = 0
nc = 0
opção = ''
cont = 0
while True:
    print('-=-'*20)
    nj = int(input('Digite um valor de 0 a 10: '))
    opção = str(input('Você quer Par ou Impar?[P/I] ')).upper().strip()[0]
    while opção not in 'PI':
        opção = str(input('Você quer Par ou Impar?[P/I] ')).upper().strip()[0]
    nc = random.randint(0, 10)
    soma = nj + nc
    result = soma % 2
    print(f'Eu escolho {nc}')
    if opção == 'I':
        if result == 1:
            print(f'A soma deu {soma}. Você Venceu!')
            cont += 1
        else:
            print(f'A soma deu {soma}. Você perdeu!')
            break
    elif opção == 'P':
        if result == 1:
            print(f'A soma deu {soma}. Você perdeu!')
            break
        else:
            print(f'A soma deu {soma}. Você venceu!')
            cont += 1
    else:
        print('Opção Invalida!')
print(f'Você venceu {cont} vezes.')


