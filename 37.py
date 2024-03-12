valor = int(input('Escolha o número para ser convertido: '))
id_conv = int(input('Escolha a base de conversão:  \n[1] para BINÁRIO \n[2] para OCTAL \n[3] para HEXADECIMAL \nEscolha sua opção: '))

if id_conv == 1: 
    vr_conv = bin(valor)
    txt = 'Binário'
elif id_conv == 2: 
    vr_conv = oct(valor)
    txt = 'Octal'
elif id_conv == 3: 
    vr_conv = hex(valor)
    txt = 'Hexadecimal'
else:
    print('Código não identificado')
print(f'Você converteu para {txt}. Resultado: {vr_conv[2:]}')