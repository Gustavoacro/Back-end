from datetime import date

ano = int(input('Que ano quer analisar, para analisar o ano da maquina inisra o 0: '))

ano_maquina = date.today().year

if ano == 0:
    ano = ano_maquina
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'o ano {ano} é BISSEXTO')
    else: 
        print(f'O ano {ano} NÂO é BISSEXTO')
        
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano {ano} é BISSEXTO')
else: 
    print(f'O ano {ano} NÂO é BISSEXTO')
   