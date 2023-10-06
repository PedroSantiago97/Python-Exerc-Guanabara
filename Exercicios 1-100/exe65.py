num = 0
op = 'S'
c = 0
lista= []
while op.upper() == 'S':
    c += 1
    num = int(input('Digite um número: '))
    lista.append(num)
    op = input('Quer continuar? [S/N]: ')

soma = int(sum(lista))
print(f'Você digitou {c} numeros e a média foi {(soma/c):.2f}.')
print(f'O maior valor foi {max(lista)} e o menor foi {min(lista)}.')

