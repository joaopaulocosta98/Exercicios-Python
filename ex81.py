opção = 'S'
lista = []
while opção == 'S':
    n = int(input('Digite o valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Número duplicado!')
    opção = input('Deseja continuar?[S/N] ').strip().upper()
    print('-*'*20)

    if opção == 'N':
        break

print(f'Você digitou o total de {len(lista)} valores!')
lista.sort(reverse=True)
print(f'Foram digitados os valores {lista} de forma descrescente.')
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O Número 5 NÃO está na lista!')

