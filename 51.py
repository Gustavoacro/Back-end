termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
decimo = termo +(10 - 1) * razao
for c in range(termo,decimo + razao,razao):
    print(c)
print('ACABOU')