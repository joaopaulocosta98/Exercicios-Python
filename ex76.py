print('--'*20)
print(f'{"TABELA DE PREÇO":^40}')#Para centralizar
print('--'*20)
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 30.00)
for pos in range(0, len(listagem)):#len é a quantidade de itens
    if pos % 2 ==0:
        print(f'{listagem[pos]:.<30}',end='')#Para colocar pontos e alinhar a esquerda
    if pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')#Para alinhar a direita