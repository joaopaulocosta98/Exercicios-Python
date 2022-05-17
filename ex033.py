from datetime import date
ano = int(input('Digite o ano para ser analizado ou Digite 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é \033[33mBISSEXTO\033[m'.format(ano))
else:
    print('O ano de {} \033[31mNÃO É\033[m BISSEXTO'.format(ano))