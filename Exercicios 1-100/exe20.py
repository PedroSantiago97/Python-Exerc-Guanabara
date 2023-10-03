
import random


pri = input("Primeiro Aluno: ")
seg = input("Segundo Aluno: ")
ter = input("Terceiro Aluno: ")
qua = input("Quarto Aluno: ")

ordem = [pri, seg, ter, qua]
random.shuffle(ordem)
print(f"A ordem de apresentação será: ")
print(ordem)

# Lista embaralhada
# random.shuffle(): Embaralha um array
# Usar o random.shuffle() antes do print(f) e mostrar a variável, não funciona dentro do print(f) T.T