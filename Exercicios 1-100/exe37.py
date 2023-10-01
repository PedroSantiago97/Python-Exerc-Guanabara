num = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

op = int(input('Sua Opção: '))

if op == 1:
    print(f'O número {num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif op == 2:
    print(f'O número {num} convertido para OCTAL é igual a {oct(num)[2:]}')
else:
    print(f'O número {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')

# Um adeno a operação de "Fatiar" em que [2:] fatia os resultados mostrando eles apartir do terceiro termo
# Pois os 2 primeiros foram fatiados !!!!





