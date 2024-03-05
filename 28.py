from random import randint # importa biblioteca do sorteador
from time import sleep # importa temporizador

num = int(input('Adivinhe o número = '))
print('PROCESSANDO...')
sleep(3)
valor_comput = randint(0, 5) #Faz com que o computador escolha um número.
if num == valor_comput:
    print(f'Você acertou! Eu pensei no {valor_comput}.')
else:
    print(f'Você errou! Tente novamente.')