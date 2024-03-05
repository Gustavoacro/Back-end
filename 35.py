reta1 = int(input('Insira o valor da reta: '))
reta2 = int(input('Insira o valor da reta: '))
reta3 = int(input('Insira o valor da reta: '))

#definição maior reta
# maior = reta1

# if reta2 > reta1 and reta2 > reta3:
#     maior = reta2
# elif reta3 > reta1 and reta3 > reta2:
#     maior = reta3

# maior_valor = maior

# soma = reta1 + reta2 + reta3 - maior_valor

# if soma > maior_valor:
#     print('Não é possivel criar um triângulo')
# else:
#     print('É possivel criar um triângulo')

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÂO podem formar um triângulo!')


