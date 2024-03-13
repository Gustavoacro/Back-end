from math import sin, radians, cos, tan
valor = int(input("Digite o ângulo: "))
print(f"O ângulo de {valor} tem o SENO de {sin(radians(valor)):5.2f}")
print(f"O ângulo de {valor} tem o COSSENO de {cos(radians(valor)):5.2f}")
print(f"O ângulo de {valor} tem a TANGENTE de {tan(radians(valor)):5.2f}")