d = int(input('Digite a quantidade de dias alugados: '))
k = float(input('Digite a quantidade de kilômetros percorridos: '))
v = d * 60 + k * 0.15
print('Com {} dias alugados e {} Km percorridos, o valor a pagar é de {:.2f}R$!'.format(d,k,v))

