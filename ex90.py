aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))
print('-='*20)
for i,v in aluno.items():
    print(f'{i}:{v}')
if aluno['média'] >= 7:
    print('APROVADO!')

elif aluno['média'] < 5:
    print('REPROVADO!')
else:
    print('RECUPERAÇÃO!')