import random
import time
num = random.randint(0,5) # número do computador
print('-=-' * 30)
print('Vamos jogar! vou pensar em um número de 0 a 5 e você precisa adivinhar.')
print('-=-' * 30)
print('Pensando em um número...')
time.sleep(3) # tempo para o computador "pensar"
res = int(input('Qual número você acha que é? ')) # número do usúario
if res == num:
    print('PARABÉNS! Você acertou.')
else:
    print('ERROU! , Eu pensei no número {}!'.format(num))

