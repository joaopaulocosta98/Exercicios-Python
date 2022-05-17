fr = str(input('Escreva a frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(fr.count('A')))
print('A letra A aparece primeiro na posição {}'.format(fr.find('A')+1))
print('A letra A aparece por ultimo na posição {}'.format(fr.rfind('A')+1))
