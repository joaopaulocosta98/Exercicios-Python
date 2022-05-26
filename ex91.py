from random import randint
from time import sleep
from operator import itemgetter
lista ={}
lista['jogador1'] = randint(1,6)
lista['jogador2'] = randint(1,6)
lista['jogador3'] = randint(1,6)
lista['jogador4'] = randint(1,6)
ranking = {}
print('-='*20)
print('JOGO DOS DADOS')
print('-='*20)
sleep(1)
for k,v in lista.items():
    print(f'{k} = {v}')
    sleep(1)
ranking = sorted(lista.items(), key=itemgetter(1),reverse=True)#para colocar os itens da docionário em ordem maior para menor
print('-='*20)
sleep(1)
for i,v in enumerate(ranking):
    print(f'{i+1} Lugar < {v[0]} com o {v[1]} sorteado >')
    sleep(1)