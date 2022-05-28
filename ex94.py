galera = []
pessoa = {}
soma = média = 0
opção = 'S'
while opção:
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo:[F/M] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!Aceito apenas "F" ou "M".')
    pessoa['idade'] =int(input('Digite a idade: '))
    soma += pessoa['idade']
    while True:
        opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if opção in 'SN':
            break
        print('ERRO!Aceito apenas "S" ou "N".')
    print('-='*20)
    galera.append(pessoa.copy())
    pessoa.clear()
    if opção == 'N':
        break
print(f'Foram cadastradas {len(galera)} pessoas.')
média = soma / len(galera)
print(f'A média de idade é de {média:5.2f} anos.')
print('As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}...')
print()
print('As pessoas com a idade a cima da média são ',end='')
for p in galera:
    if p['idade'] >= média:
        print('   ')
        for k,v in p.items():
            print(f'{k} = {v};',end=' ')
        print()
print('<<ENCERRADO>>')
