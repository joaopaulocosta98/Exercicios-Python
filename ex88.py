from random import randint
from time import sleep
print('-='*15)
print('         MEGA SENA')
print('-='*15)
quant = int(input('Quantos jogos você deseja sortear? '))
tot = 1
lista = []
jogos = []
while tot <= quant:
    contador = 0
    while True:
        num = randint(1, 60)#para sortear um número
        if num not in lista:
            lista.append(num)#se esse número não estiver na lista, adicionar
            contador += 1#para contador os números sorteados
        if contador >= 6:#quando sortear 6 números, parar de sortear
            break
    lista.sort()
    jogos.append(lista[:])#para copiar a lista de 6 números dentro de outra lista
    lista.clear()#para limpar a lista de 6 números e gerar um nova
    tot += 1#para contar a quantidade de jogos que foi escolhido pelo usuario
print('-='*5, f'SORTEANDO {quant} JOGOS', '-='*5)
print()
for i, l in enumerate(jogos):#para separar cada lista de 6 números dentro de lista de jogos
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print()
print('-='*15)
print('           JOGOS SORTEADOS')
print('-='*5,'BOA SORTE!','-='*5)


