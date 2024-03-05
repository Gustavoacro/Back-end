from time import sleep

va_cs = float(input('Insira o valor do imóvel: '))
salario = float(input('Insira o seu salário: '))
qt_anos = int(input('Insira em quantos deseja quitar: '))

qt_parc = qt_anos * 12 

porcent = 30 * salario / 100

parc_final = va_cs / qt_parc

print('Calculando...')
sleep(3)

if parc_final <= porcent:
    print(f'Parabéns, seu empréstimo foi \033[1;32;42mACEITO\033[0m. Ficaram {qt_parc} parcelas de {parc_final:.2f}')
else:
    print(f'Poxa, seu empréstimo foi NEGADO. Seu salário ultrapassou o teto de 30%.')