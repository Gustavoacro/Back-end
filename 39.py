from datetime import date

dt_nasc = int(input('Insira seu ano de nascimento: '))

# Calculo ano atual
result = (dt_nasc - date.today().year) * -1

if result == 18:
    print(f'Você possui {result} anos e deve se alistar em {date.today().year}.')
elif result < 18:
    soma = result - 18
    print(f'Você possui {result} anos e deve se aliastar em {date.today().year - soma }.')
elif result > 18:
    soma = result - 18
    print(f'Você possui {result} anos e deveria ter se alistado em {date.today().year - soma}')




