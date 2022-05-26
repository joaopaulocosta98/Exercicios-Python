lista =[]
for c in range(0, 5):
    n = int(input('Informe o Valor: '))
    if c == 0 or n > lista[-1]:#Se o n for maior do que o ultimo elemento
        lista.append(n)
        print('Adicionado ao fim da lista...')
    else:
        posição = 0
        while posição < len(lista):
            if n <= lista[posição]:
                lista.insert(posição, n)
                print(f'Adicionado na posição {posição + 1} da lista...')
                break
            posição += 1
print(f'Você digitou os números {lista}')



