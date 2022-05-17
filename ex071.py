nome = preço = menor = soma = mais = cont = 0
nommenor = ' '
cont = 0
while True:
    print('-=-'*20)
    nome = str(input('Informe o nome do produto:'))
    preço = float(input('Informe o valor do produto:R$'))
    soma += preço
    cont += 1
    if cont == 1:
        menor = preço
        nommenor = nome
    else:
        if preço < menor:
            menor = preço
            nommenor = nome
    if preço > 1000:
        mais += 1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if opção in 'N':
        break
print('-=-'*20)
print(f'''Foram adicionados {cont} itens, com o total de R${soma:.2f}.
{mais} produtos custam mais de R$1000.
E o menor valor foi {nommenor} de R${menor:.2f}''')
