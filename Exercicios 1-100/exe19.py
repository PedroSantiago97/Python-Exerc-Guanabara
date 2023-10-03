import random

pri = input("Primeiro Aluno: ")
seg = input("Segundo Aluno: ")
ter = input("Terceiro Aluno: ")
qua = input("Quarto Aluno: ")

sorteio =[pri, seg, ter, qua]
sorteado = random.randint(0, len(sorteio)-1)
print(f"O aluno escolhido foi {sorteio[sorteado]}")


# Primeiro contato com Arrays em Python =D
# Objeto criado com Inputs coletadas do usuário
# Usei random.randint pra escolher aleatóriamente um valor numérico
# Usei len() pra ver a quantidade de itens e diminui - 1 pra obter a sua posição no array

"""sorteio =[pri, seg, ter, qua]
sorteado = random.choice(sorteio)
print(f"O aluno escolhido foi {sorteado}")

# Pode ser feito com a função random.choice(), sorteando uma string diretamente e imprimindo ela."""


