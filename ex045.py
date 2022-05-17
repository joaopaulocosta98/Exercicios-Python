print('{:=^40}'.format('LOJAS COSTA'))
valor = float(input('Digite o valor do produto:R$ '))
print('''Informe a opção de pagamento:'
[1] Para à vista Dinheiro/Cheque.
[2] Para à vista no cartão.
[3] Em até 2x no cartão.
[4] 3x ou mais no cartão.''')
opção = int(input('Qual a sua escolha? '))
if opção == 1:
    v1 = valor - (valor * 10 / 100)
    print('O valor fica R${:.2f} com 10% de desconto!'.format(v1))
elif opção == 2:
    v1 = valor - (valor * 5 / 100)
    print('O valor fica R${:.2f} com 5% de desconto!'.format(v1))
elif opção == 3:
    v1 = valor / 2
    print('O valor fica R${:.2f} com duas parcelas de R${:.2f}'.format(valor,v1))
elif opção == 4:
    v1 = valor + ( valor * 20 / 100 )
    parcelas = int(input('Quantas parcelas? '))
    v2 = v1 / parcelas
    print(' O valor fica R${:.2f} com 20% de juros, dividido em {} parcelas de R${:.2f}'.format(v1, parcelas, v2))
else:
    print('\033[31mOpção invalida!\033[m')
