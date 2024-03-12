from time import sleep

#Entrada de dados
va_cs = float(input('Insira o valor do imóvel: '))
salario = float(input('Insira o seu salário: '))
qt_anos = int(input('Insira em quantos deseja financiar: '))

qt_parc = qt_anos * 12 #Conversor meses p/ anos

minimo = 30 * salario / 100 # Cálculo porcentagem

parc_final = va_cs / qt_parc #Cálculo valor parcela

print('Calculando...')
sleep(3)

if parc_final <= minimo:
    print(f'Parabéns, seu empréstimo foi \033[1;32;0mACEITO\033[0m. Ficaram {qt_parc} parcelas de {parc_final:.2f}')
else:
    print(f'Poxa, seu empréstimo foi \033[1;31;0mNEGADO\033[0m. O valor de {va_cs:.2f} do imóvel em {qt_anos} anos ficou em {parc_final:.2f}/mês ultrapassando os 30% de seu salário.')