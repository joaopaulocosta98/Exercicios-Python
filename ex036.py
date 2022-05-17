print('\033[31m-=-\033[m' * 20)
print('\033[33mANALIZADOR DE TRIÂNGULO\033[m')
print('\033[31m-=-\033[m' * 20)
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite o ultimo valor: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com os valores informados \033[33mÉ POSSÍVEL\033[m formar um triângulo.')
else:
    print('Com os valores informas \033[31mNÃO É POSSÍVEL\033[m formar um triângulo.')
