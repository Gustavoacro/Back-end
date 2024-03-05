salario = float(input('Insira o valor de seu salário: '))

if salario > 1250:
    novo = (10*salario) / 100 + salario
elif salario <=1250:
    novo = (15*salario) / 100 + salario
    
print(f'O seu novo salário é: {novo:.2f}')