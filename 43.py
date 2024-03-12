peso = float(input('Insira o seu peso: '))
altura = float(input('Insira sua altua: '))

calc_imc = (peso/altura) /altura

if calc_imc < 18.4:
    print(f'Abaixo do Peso{calc_imc:.1f}')
elif calc_imc >= 18.5 and calc_imc <= 24.9:
    print(f'Peso ideal{calc_imc:.1f}')
elif calc_imc >= 25 and calc_imc <= 29.9:
    print(f'Sobrepeso {calc_imc:.1f}')
elif calc_imc >= 30 and calc_imc <= 39.9:
    print(f'Obesidade {calc_imc:.1f}')
else:
    print(f'Obesidade mórbida {calc_imc:.1f}')