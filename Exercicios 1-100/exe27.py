nome = (input('Digite seu nome completo: '))

separado = nome.split(' ')
# Sempre que usar .split() criar uma variável pra criar a varipavel modificada

print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {separado[0]}')
print(f'Seu ultimo nome é {separado[len(separado)-1]}')

# Sempre que mecher com Arrays se atentar ao fato da sequencia começar no 0 e o .len() começa a contar do 1 !!! 




