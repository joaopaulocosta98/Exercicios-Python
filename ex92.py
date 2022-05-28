from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input("Digite o nome: ")).strip()
ano = int(input('Digite o ano de nascimento: '))
cadastro['idade'] = datetime.now().year - ano
cadastro['ctps'] = int(input('Digite o número da Carteira de Trabalho (0 não tem):  '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Digite o ano de contratação: '))
    cadastro['salário'] = float(input(('Digite o salário: R$')))
    cadastro['aposentadoria'] = ((cadastro['contratação'] + 35) - datetime.now().year) + cadastro['idade']
print('-=-'*20)
print('CADASTRADO!')
for k, v in cadastro.items():
    print(f'{k} = {v}')