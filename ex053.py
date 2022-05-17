total = 0
num = int(input('Digite um número intero: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número foi dividido {} vezes.'.format(total))
if total == 2:
    print('Esse número é primo!')
else:
    print('Esse número não é primo!')