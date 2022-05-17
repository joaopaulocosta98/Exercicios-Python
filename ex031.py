num = int(input('Digite um número: '))
resul = num % 2
if resul == 1 :
    print('O número {} é \033[33mÍmpar\033[m!'.format(num))
else:
    print('O número {} é \033[34mPar\033[m!'.format(num))




