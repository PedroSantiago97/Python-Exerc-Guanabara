
import math

an = float(input("Digite o ângulo que você deseja: "))

print(f"O ângulo de {an} tem o SENO de {math.sin(math.radians(an)):.2f}")
print(f"O ângulo de {an} tem o COSSENO de {math.cos(math.radians(an)):.2f}")
print(f"O ângulo de {an} tem a TANGENTE de {math.tan(math.radians(an)):.2f}")


# math.sin, math.cos e math.tan: Mostram o seno, cosseno e tangende de um objeto, respectivamente
# math.radians: coloca o objeto digitado em radiano
# OBS: Se for calcular angulos, colocar o objeto recebido em radiano !!!!

