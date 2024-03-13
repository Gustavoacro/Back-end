valor = float(input('Insira o valor para ser calculado o desconto: '))
desconto = ((5 * valor)/ 100)
print(f'O desconto foi de: {desconto:5.2f} R$. E o valor final foi de: {(desconto - valor)* -1:5.2f} R$.')