from math import factorial

print('Digite um número para ')
num = int(input('calcular seu Fatorial: '))
c = num
print(f'Calculando {num}! = ', end='')
while c > 0:
    # Enquanto o c, que é igual ao num digitador, for 0
    # Imprimir, na linha, o proprio c
    print(f'{c}', end='')
    if c > 1:
        # Se o c foi um valor maior que 1, coloca um x do lado esquerdo, na mesma linha, pra representar a multiplicação
        print(' x ', end='')
    else:
        # se o c Não foi maior que 1, quer dizer que chegou a 0, logo colocar o sinal de igual
        # Atentar ao fato de end='' Deixar todos eles na mesma linha na hora de execução, mesmo nao estando dentro do laço nem na condicional ;)
        print(' = ', end='')
    c-=1
print(f'{factorial(num)}', end='')

# Estrutura de repetição usada pra mostrar o calculo de fatorial
# Neste exemplo, definimos end como um espaço em branco, para que a segunda chamada de print() não comece em uma nova linha, mas continue na mesma linha da primeira chamada.




