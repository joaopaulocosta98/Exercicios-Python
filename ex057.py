soma = 0
media = 0
hmaisvelho = 0
nomehmaisveho = ''
mulher20 = 0
for c in range(1, 5):
    print('-------{}ªPESSOA--------'.format(c))
    nome = str(input('Informe seu nome: '))
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip()
    print('-=-'*20)
    soma += idade
    if c == 1 and sexo in 'Mm':
        hmaisvelho = idade
        nomehmaisveho = nome
    if sexo in 'Mm' and hmaisvelho < idade:
        hmaisvelho = idade
        nomehmaisveho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
media = soma / 4
print('O homem mais velho se chama {} e tem {} anos.'.format(nomehmaisveho,hmaisvelho))
print('Á média é de {} anos'.format(media))
print('E temos {} mulheres com menos de 20 anos.'.format(mulher20))

