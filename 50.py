cont = 0
for leia in range(1,7):
    valor = int(input(f'Insira o {leia}° valor inteiro: '))
    if valor % 2 == 0 and valor <= 9:
        cont += valor
print(cont)