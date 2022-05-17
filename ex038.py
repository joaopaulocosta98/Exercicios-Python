num = int(input('Digite um número inteiro: '))
print('''Escolha umas das opções:
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL''')
opcão = int(input('Sua escolha é: '))
if opcão == 1:
    print('O número {} em BINÁRIO é {}.'.format(num,bin(num)[2:]))
elif opcão == 2:
    print('O número {} em OCTAL é {}.'.format(num,oct(num)[2:]))
elif  opcão == 3:
    print('O número {} em HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('\033[31mOpção inválida!\033[m')