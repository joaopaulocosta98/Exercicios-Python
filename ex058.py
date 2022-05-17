sexo = str(input('Qual o seu sexo?[M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informação errada! digite novamente! Qual o seu sexo?[M/F] ')).strip().upper()[0]
print('Fim!')