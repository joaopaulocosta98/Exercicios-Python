opção = 'S'
maior = 0
homens = 0
mul = 0
cont = 0
while True:
    while opção == 'S':
        print('-=-' * 20)
        idade = int(input('Digite a idade: '))
        sexo = ' '
        while sexo not in 'MF':
           sexo = str(input('Informe o seu sexo:[M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homens += 1
        if idade >= 18:
            maior += 1
        if idade < 20 and sexo == 'F':
            mul += 1
        opção = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
        cont += 1
    if opção == 'N':
        break
print(f'Foram cadastradas {cont} pessoas, {homens} são homens, {maior} pessoas são maiores de 18.')
print(f'E {mul} mulheres são menores de 20 anos.')
