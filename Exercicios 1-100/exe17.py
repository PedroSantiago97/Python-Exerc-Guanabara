
import math

catop = float(input("Comprimento do cateto oposto: "))
catad = float(input("Comprimento do cateto adjacente: "))

print(f"A hipotenusa vai medir {math.hypot(catop, catad):.2f}")

# print(f"A hipotenusa vai medir {math.sqrt((catop**2)+(catad**2)):.2f}")

# math.sqrt: tira a raiz quadrada de um objeto de número
# math.hypot: tira a hipotenusa mediante o valor de 2 variaveis colocadas em ()