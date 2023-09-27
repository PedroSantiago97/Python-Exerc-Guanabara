num = input('Informe um número: ')

print(f'Analisando o número {num} temos: ')

uni = ['Unidade']
deze = ['Dezena', 'Unidade']
centena = ['Centena', 'Dezena', 'Unidade']
mil = ['Milhar', 'Centena', 'Dezena', 'Unidade']
dezmil = ['Dezena de Milhar', 'Milhar', 'Centena', 'Dezena', 'Unidade']
cenmil = ['Centena de Milha','Dezena de Milhar', 'Milhar', 'Centena', 'Dezena', 'Unidade']

if len(num) == 1:
    print(f'{uni[0]}:{num[0]}')
if len(num) == 2:
    print(f'{deze[0]}:{num[0]}')
    print(f'{deze[1]}:{num[1]}')
if len(num) == 3:
    print(f'{centena[0]}:{num[0]}')
    print(f'{centena[1]}:{num[1]}')
    print(f'{centena[2]}:{num[2]}')
if len(num) == 4:
    print(f'{mil[0]}:{num[0]}')
    print(f'{mil[1]}:{num[1]}')
    print(f'{mil[2]}:{num[2]}')
    print(f'{mil[3]}:{num[3]}')
if len(num) == 5:
    print(f'{dezmil[0]}:{num[0]}')
    print(f'{dezmil[1]}:{num[1]}')
    print(f'{dezmil[2]}:{num[2]}')
    print(f'{dezmil[3]}:{num[3]}')
    print(f'{dezmil[4]}:{num[4]}')
if len(num) == 6:
    print(f'{cenmil[0]}:{num[0]}')
    print(f'{cenmil[1]}:{num[1]}')
    print(f'{cenmil[2]}:{num[2]}')
    print(f'{cenmil[3]}:{num[3]}')
    print(f'{cenmil[4]}:{num[4]}')
    print(f'{cenmil[5]}:{num[5]}')

if num == ' ':
    print('Digite um número valido')
    


