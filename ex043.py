print('\033[33m-=-\033[m'*20)
print('ANALIZADOR DE TRIÂNGULO')
print('\033[33m-=-\033[m'*20)
l1 = float(input('Digite o valor do lado: '))
l2 = float(input('Digite o valor de outro lado: '))
l3 = float(input('Digite o valor de mais um lado: '))
if l1 < l2 + 3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Com os lados de {}, {} e {} é possivel formar um triângulo;'.format(l1,l2,l3))
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possivel formar um triângulo!')

