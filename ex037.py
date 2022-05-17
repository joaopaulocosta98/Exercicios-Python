vc = float(input('Informe o valor da casa: R$'))
sc = float(input('Informe o salário do comprador: R$'))
ap = int(input('Informe a quantidade de anos que deseja para pagar: '))
prest = vc / (ap * 12)
print('Para pagar a casa do valor de {:.2f}, a prestação será de {:.2f} em {} anos.'.format(vc,prest,ap))
min = sc * 30 / 100
if prest <= min:
    print('\033[32mEMPRESTIMO ACEITO!\033[m')
else:
    print('\033[31mEMPRESTIMO NEGADO!\033[m')