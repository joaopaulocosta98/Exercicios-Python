from random import randint
from time import sleep
tent = 1
print('=' * 20)
print('VAMOS JOGAR! TENTE ADIVINHAR EM QUAL NÚMERO DE 0 A 10 EU ESTOU PENSADO.')
print('=' * 20)
print('Pensando em um número...')
sleep(1.5)
comp = randint(0, 10)
num = int(input('Qual número você acha que é?'))
while num != comp:
    if num < comp:
        num = int(input('Mais! tente novamente:'))
    else:
        num = int(input('Menos! tente novamente:'))
    tent += 1
print('ACERTOU! E VOCÊ PRECISOU DE {} TENTATIVAS PARA CONSEGUIR'.format(tent))


