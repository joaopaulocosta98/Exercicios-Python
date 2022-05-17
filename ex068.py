n = 0
while True:
    print('-=-' * 20)
    n = int(input('Digite um valor para saber a sua tabuada: '))
    if n > 0:
        for c in range (1 , 11):
            print(f'{n} X {c} = {c * n}')
    if n < 0:
        break
print('-=-'*20)
print('Fim!')



