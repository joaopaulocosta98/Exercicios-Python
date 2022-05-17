peso = float(input('Informe o seu peso: (kg) '))
altura = float(input('Informe a sua altura: (m) '))
imc = peso / (altura ** 2)
print('Seu Indíce de Massa Corporal é {:.2f}.'.format(imc))
if imc < 18.5:
    print('\033[33mVocê está abaixo do peso!\033[m')
elif 18.5 <= imc < 25:
    print('\033[32mVocê está no peso ideal!\033[m')
elif 25 <= imc < 30:
    print('\033[33mVocê está no sobrepeso!\033[m')
elif 30 <= imc < 40:
    print('\033[35mVocê está na Obesidade!\033[m')
elif imc >= 40:
    print('\033[31mVocê está na Obesidade Mórbida!\033[m')