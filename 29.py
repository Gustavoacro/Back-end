from time import sleep

velocidade = int(input('Insira sua velocidade para análise = ')) #Entrada de dados

print('Calculando...')
sleep(3) #Temporizador

calc_multa = (velocidade - 80) * 7 #Calculo de velocidade

if velocidade > 80:
    print(f'Você ultrapassou o limite de velocidade e foi multado em: R${calc_multa:5.2f}.')
else:
    print('Você está dentro da velocidade permitida.')