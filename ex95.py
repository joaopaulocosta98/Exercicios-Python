time = []
jogador = {}
jogos = []
opção = 'S'
while opção:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogos.clear()
    for c in range(0,partidas):
        jogos.append(int(input(f' - Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = jogos[:]
    jogador['total'] = sum(jogos)#para somar o que está em jogos
    time.append(jogador.copy())
    while True:
        opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if opção in 'SN':
            break
        print('ERRO!Aceito apenas "S" ou "N".')
    if opção == 'N':
        break
    print('-='*20)
print('-='*20)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end=' ')
print()
print('--'*20)
for k,v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--'*20)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para encerrar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO!Não existe jogador de código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} --')
        for i,g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i + 1} fez {g} gols;')
    print('-='*20)

