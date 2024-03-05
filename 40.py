n1 = float(input('Insira sua nota: '))
n2 = float(input('Insira sua segunda nota: '))

media = (n1 + n2) /2

if media <= 4.9:
    print('REPROVADO')
elif media >= 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 7.0:
    print ('APROVADO')
