# Com importação
from math import trunc
num = float(input("Escreva um valor: "))
print(f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}")
# Sem importação
num = float(input("Escreva um valor: "))
print(f"O valor digitado foi {num} e a sua porção inteira é {int(num)}")