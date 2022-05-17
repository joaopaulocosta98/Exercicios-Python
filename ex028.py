nom = str(input('Digite o seu nome completo: ')).strip()
n1 = nom.split()
print('Seu primeiro nome é {}'.format(n1[0]))
print('Seu ultimo nome é {}'.format(n1[len(n1)-1]))
