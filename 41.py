from datetime import date

dt_nasc = int(input('Insira seu ano de nascimento: '))

result = (dt_nasc - date.today().year) * -1

if result <= 9:
    print('Sua categoria é: MIRIM')
elif result >= 10 and result <= 14:
    print('Sua categoria é: INFANTIL')
elif result >= 15 and result <= 19:
    print('Sua categoria é: JUNIOR')
elif result == 20:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER') 