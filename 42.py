reta1 = int(input('Insira o valor da reta: '))
reta2 = int(input('Insira o valor da reta: '))
reta3 = int(input('Insira o valor da reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Os segmentos acima NÂO podem formar um triângulo!')
