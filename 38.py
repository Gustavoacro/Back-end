v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))

if v1 > v2:
    print(f'O {v1} é maior que {v2}.')
elif v2 > v1:
    print(f'O {v2} é maior que {v1}.')
else:
    print(f'O {v1} é igual ao {v2}.')