
valor1 = int(input('Insira o valor = '))
valor2 = int(input('Insira o segundo valor = '))
valor3 = int(input('insira o terceiro valor = '))

menor = valor1

if valor2 < valor1 and valor2 < valor3:
    menor = valor2
elif valor3 < valor1 and valor3 < valor2:
    menor = valor3

#verificando maior valor
maior = valor1  

if valor2 > valor1 and valor2 >valor3:
    maior = valor2
elif valor3 > valor1 and valor3 > valor2:
    maior = valor3
print(f'O menor valor é {menor}')
print(f'O maior valor é {maior}')




