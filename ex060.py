from time import sleep
n1 = int(input('Informe o primeiro valor:'))
n2 = int(input('Informe o segundo valor:'))
escolha = 0
while escolha != 5:
    print('''Escolha entre as opções;
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    escolha = int(input("Qual a sua escolha? "))
    if escolha == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1,n2, (n1 + n2)))
    elif escolha == 2:
        print('{} vezes {} é igual a {}'.format(n1, n2, (n1 * n2)))
    elif escolha == 3:
        if n1 > n2:
            print('{} é o maior!'.format(n1))
        elif n1 < n2:
            print('{} é o maior!'.format(n2))
        elif n1 == n2:
            print('Os dois valores são iguais!')
    elif escolha == 4:
        n1 = int(input('Informe o primeiro valor:'))
        n2 = int(input('Informe o segundo valor:'))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção invalida! Tente novamente.')
    print('=' * 20)
    sleep(2)
print('Fim do programa! Obrigado!')




