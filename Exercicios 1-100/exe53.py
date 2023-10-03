frase = input('Digite uma frase: ')
frase1 = frase.replace(" ", '')
frase_invertida = (frase1[::-1])

print(f'O inverso de {frase1} é {frase_invertida} .')

if frase1 == frase_invertida:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')

# Metodo para separar o espaço da frase feito com o .replace( , )
# Frase invertida com [::-1]: isso inverte oa ordem dos termos do objeto, A notação é [início:fim]

