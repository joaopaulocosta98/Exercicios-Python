from time import sleep
def contador(a, b, c):
    if c < 0:#para se caso o passe for negativo
        c *= -1
    if c == 0:
        c = 1
    print('~' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(1)
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}',end=' ',flush=True)
            cont += c
            sleep(0.5)
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ',flush=True)
            cont -= c
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('~' * 20)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
pas = int(input('Passo: '))
contador(i, f, pas)