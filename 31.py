distancia = float(input('Informe a distância de sua viagem: '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O valor de sua passagem ficará em: {preco:5.2f}')