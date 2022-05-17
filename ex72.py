cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
        'dezoito', 'dezenove', 'vinte')
opção = 'S'
while opção =='S':
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {cont[numero]}')
        opção = input('Deseja continuar?[S/N]').upper()

    else:
        print('Tente novamente!', end=' ')
        opção = input('Deseja continuar?[S/N]').upper()
print('Até mais...')