from datetime import date
an = int(input('Informe o ano de Nascimento: '))
idade = date.today().year - an
print('Sua idade é de {} anos.'.format(idade))
if idade > 25:
    print('Você é da categoria MASTER!')
elif 25 >= idade > 19:
    print('Você é da categoria SÊNIOR!')
elif 19 >= idade > 14:
    print('Você é da categoria JÚNIOR!')
elif 14 >= idade > 9:
    print('Você é da categoria INFANTIL!')
elif 9 >= idade :
    print('Você é da categoria MIRIM!')
