opção = ''
média = 0
cont = 0
soma = 0
n = int
lista = []
while opção != 'N':
    n = int(input('Informe o número: '))
    opção = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    soma = soma + n
    cont = cont + 1
    lista = lista + [n]
medtot = soma / cont
maior = max(lista)
menor = min(lista)
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
print('Finalizando... com o média de {:.2f}'.format(medtot))