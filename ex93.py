jogador = {}
jogos = []
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,partidas):
    jogos.append(int(input(f' - Quantos gols na partida {c + 1}? ')))
jogador['gols'] = jogos[:]
jogador['total'] = sum(jogos)#para somar o que está em jogos
print('-=-'*30)
print(jogador)
print('-=-'*30)
for k,v in jogador.items():
    print(f'{k} = {v}')
print('-=-'*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas!')
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i+1} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


