números = (int(input("Digite um número: ")),
           int(input("Digite outro número: ")),
           int(input("Digite mais um número: ")),
           int(input("Digite o ultimo número: ")),)
if 9 in números:
    print(f'O número nove apareceu {números.count(9)} vezes')#.count pata contar quantas vezes o informado aparece!
else:
    print('Não foi digitado o número nove!')
if 3 in números:
    print(f'O número três apareceu na {números.index(3)+1} posição')#.index para informar a posição do que foi informado.
else:
    print('Não foi digitado o número três!')
print('Os números pares são ',end=' ')
for n in números:
    if n % 2 == 0:
        print(n,end=' ')



