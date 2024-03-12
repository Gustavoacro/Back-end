from time import sleep 
from random import randint 

jogada = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0,2)

print('''Suas opções são: 
[0]Pedra
[1]Papel
[2]Tesoura''')
id_jogador = int(input('Insira sua jogada: '))

if id_jogador <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)

    print(f'Sua jogada foi {jogada[id_jogador]}')
    print(f'O computador jogou {jogada[computador]}')
    print('-=' * 20)

    if computador == 0:
        if id_jogador == 0:
            print('Empate')
        elif id_jogador == 1:
            print('Jogador venceu')
        elif id_jogador == 2:
            print('Computador venceu')
    if computador == 1:
        if id_jogador == 0:
            print('Computador venceu')
        elif id_jogador == 1:
            print('Empate')
        elif id_jogador == 2:
            print('Jogador venceu')
    if computador == 2:
        if id_jogador == 0:
            print('Jogador venceu')
        elif id_jogador == 1:
            print('Computador venceu')
        elif id_jogador == 2:
            print('Empate')
else:
    print('Opção não identificada')

