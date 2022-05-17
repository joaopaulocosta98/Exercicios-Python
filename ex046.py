import random
import time
print('-=-'*20)
print('VAMOS JOGAR!')
itens = ('PEDRA','PAPEL','TESOURA')
pc = random.randint(0,2)
print('''VOCÊ PODE ESCOLHER!
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('QUAL A SUA JOGADA? '))
print('-=-'*20)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!!')
time.sleep(1)
print('-=-'*20)
print('EU ESCOLHI {}!'.format(itens[pc]))
print('VOCÊ ESCOLHEU {}!'.format(itens[jogador]))
print('-=-'*20)
if pc == 0:
    if jogador == 1:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif jogador == 2:
        print('\033[31mEU GANHEI!\033[m')
    elif jogador == 0:
        print('\033[33mEMPATOU!33m')
    else:
        print('OPÇÃO INVALIDA!')
elif pc == 1:
    if jogador == 0:
        print('\033[31EU GANHEI!\033[m')
    elif jogador == 2:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif jogador == 1:
        print('\033[33EMPATOU!\033[m')
    else:
        print('OPÇÃO INVALIDA!')
elif pc == 2:
    if jogador == 1:
        print('\033[31mEU GANHEI!\033[m')
    elif jogador == 0:
        print('\033[32mVOCÊ GANHOU!\033[m')
    elif jogador == 2:
        print('\033[33mEMPATOU!\033[m')
    else:
        print('OPÇÃO INVALIDA!')
print('-=-'*20)


