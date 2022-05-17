n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
md = (n1 + n2) / 2
print('A sua média é {:.1f}'.format(md))
if md >= 7:
    print('\033[32mPARABÉNS! Você foi APROVADO!\033[m')
elif md < 5:
    print('\033[31mQUE PENA! Você foi REPROVADO!\033[m')
elif md >= 5 and md <= 6.9:
    print('\033[33mQUASE! Você ficou de RECUPERAÇÃO!\033[m')