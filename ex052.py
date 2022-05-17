termo = int(input('Digite o Termo: '))
razão = int(input('Digite a Razão: '))
dc = termo + (10 - 1) * razão
for c in range(termo, dc + razão, razão):
    print(c, end=' ')