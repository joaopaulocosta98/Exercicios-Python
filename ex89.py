ficha = []
opção = 'S'
while opção:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1+nota2) / 2
    ficha.append([nome,[nota1,nota2], media])
    opção = str(input('Deseja continuar?[S/N] ')).strip().upper()
    print('-='*20)
    if opção == 'N':
        break
print(f'{"No.":<4}{"NOME:":<10}{"MÉDIA:":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    ntaluno = int(input('Mostrar nota de qual aluno?(999 interrompe) '))
    if ntaluno == 999:
        break
    if ntaluno <= len(ficha) - 1:
        print(f'Notas de {ficha[ntaluno][0]} são {ficha[ntaluno][1]}')
        print('-='*20)
print('ATÉ MAIS!')

