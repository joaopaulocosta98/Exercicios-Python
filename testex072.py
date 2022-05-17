opção = 'S'
while opção in 'S':
    print('-=-'*20)
    valor = int(input('Informe o valor a ser sacado: R$'))
    total = valor
    totced = 0
    ced = 50
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} de R${ced}.')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 1
            totced = 0
            if total == 0:
                break
    opção = str(input('Deseja sacar mais algum valor?[S/N]')).strip().upper()[0]
    while opção not in 'SN':
        opção = str(input('Deseja sacar mais algum valor?[S/N]')).strip().upper()[0]
    if opção == 'N':
        break
print('Obrigado e tenha um Bom dia!')