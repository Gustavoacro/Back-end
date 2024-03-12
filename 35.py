reta1 = int(input('Insira o valor da reta: '))
reta2 = int(input('Insira o valor da reta: '))
reta3 = int(input('Insira o valor da reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
     if reta1 == reta2 == reta3:
        print('As medidas acima forma um triangulo Equilátero')
     elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('As medidas acima formam um triangulo Isósceles')
     else:
        print('As medidas acima formam um triangulo Escaleno')
else:
    print('Os segmentos acima NÂO podem formar um triângulo!')
 



