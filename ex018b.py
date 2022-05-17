import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co,ca)
print ('O valor da hipotenusa é {:.2f}'.format(hi))

