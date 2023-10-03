frase = input("Digite uma frase: ").upper().strip()

print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"A primeira vez que e letra A aparece é na posição: {frase.find('A')+1} ")
print(f"A ultima vez que e letra A aparece é na posição: {(frase.rfind('A')+1)-(frase.count(' '))}")

# Usuário é a pior raça que tem, ele vai fazer de tudo pro seu programa nao funcionar - Guanabara, Gustavo
# Mais exercicios de fixação sobre os parametros .find(), .count(), .upper() e .strip()
