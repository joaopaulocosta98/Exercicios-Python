palavras =("AMENDOIN","ARVORE","PESSEGO","LARANJA","CARRO")
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')