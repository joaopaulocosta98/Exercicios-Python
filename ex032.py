import time
preç = float(input('Digite a distância da viagem:'))
if preç <= 200:
    valor = preç * 0.50
else:
    valor = preç * 0.45
print('\033[7:30mCalculando o valor da passagem...\033[m')
time.sleep(3)
print('Em uma viagem de {}Km'.format(preç))
print('\033[31mO valor da passagem é R${:.2f}\033[m'.format(valor))
