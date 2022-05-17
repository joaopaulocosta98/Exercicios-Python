print('-'*20)
print('VERIFICADOR DE MULTAS')
print('-'*20)
vel = float(input('Digite a velocidade ao passar no radar: '))
if vel > 80:
    print('\033[4;31mVocê foi multado por exceder o limite de 80km/h.\033[m')# com cor vermelha
    print('\033[1;31mMulta de R${:.2f}\033[m'.format((vel - 80) * 7))# com cor vermelha
print('\033[33mTenha um bom dia! dirija com segurança!\033[m')# com cor amarela

