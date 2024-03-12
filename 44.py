valor = float(input('Insira o valor a ser pago: '))
id_oper = int(input('''[1] Dinheiro e Cheque
[2] À vista no cartão 
[3] 2x no cartão 
[4] 3x ou mais no cartão
Insira o código da operação: '''))

if id_oper == 1:
    vr_final = ((10*valor) / 100 - valor) * -1
    txt = 'Houve um desconto de 10% pelo pagamento em DINHEIRO/CHEQUE.'
elif id_oper == 2:
    vr_final = ((5*valor) / 100 - valor) * -1
    txt = 'Houve um desconto de 5% pelo pagamento à vista no CARTÂO. '
elif id_oper == 3:
    vr_final = valor/2
    txt = 'Parcelando em 2x não há acrécimo.'
elif id_oper == 4:
    vr_final = ((20*valor) / 100 + valor)
    txt = 'Parcelando 3x ou mais, há acrécimmo de 20%.'
else:
    print('Opção invalida')
print(f'{txt} O valor a ser pago é: {vr_final:.2f}')


