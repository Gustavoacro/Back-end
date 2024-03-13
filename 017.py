import math
co = float(input("Digite o cateto oposto: "))
ca = float(input("Digite o cateto adjacente: "))
# hi = (co ** 2 + ca ** 2) ** (1/2)
hi = math.hypot(co, ca)
print(f"A hipotenusa vai medir {hi:5.2f}")

