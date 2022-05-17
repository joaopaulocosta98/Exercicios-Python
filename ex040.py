from datetime import date
print('''Qual o seu sexo?
[1] para Masculino
[2] para Feminino''')
opção = int(input('Sua escolha é: '))
ano = int(input('Digite o ano de nascimento: '))
idade =date.today().year - ano
if opção == 2:
    print('Você não precisa se alistar!')
elif idade < 18:
    print('quem nasceu em {} tem {} anos!'.format(ano,idade))
    print('Ainda faltam {} anos para se alistar!'.format(18 - idade))
    print('Você deve se alistar em {}'.format((18 - idade) + date.today().year))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos'.format(ano,idade))
    print('Está na hora de se alistar!')
elif idade > 18:
    print('Quem nasceu em {} tem {} anos'.format(ano, idade))
    print('Ja passou da hora de se alistar!')
    print('Você deveria ter se alistado a {} anos atrás'.format(idade - 18))
    print('Seu alistamento foi em {}'.format((idade - 18) - date.today().year))
