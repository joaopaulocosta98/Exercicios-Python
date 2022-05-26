expr = str(input('Digite uma expressão: '))
pilha = []
for sim in expr:#para identificar cada item da string
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:#para saber se a pilha está vazia
            pilha.pop()#remover o ultimo elemento
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')