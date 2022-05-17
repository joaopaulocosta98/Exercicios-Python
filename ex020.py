import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
list = [n1,n2,n2,n4]
re = random.choice(list)
print ('O aluno escolhido foi {}'.format(re))

