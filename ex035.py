sal = float(input('Digite o valor do salário: '))
if sal > 1250.00:
    val1 = sal * 10 / 100 + sal
else:
    val1 = sal * 15 / 100 + sal
print('Com o aumento, o salário fica \033[33mR${:.2f}\033[m'.format(val1))