num = [int(input("Digite um número para a posição 1: ")),int(input("Digite um número para a posição 2: ")),
           int(input("Digite um número para a posição 3: ")),int(input("Digite um número para a posição 4: "))]
menor = min(num)
maior = max(num)
print(f'O maior número digitado foi o {maior} na posição {num.index(maior) + 1}')
print(f'O menor número digitado foi o {menor} na posição {num.index(menor) + 1}')

