nums = []
par = []
spar = []

while True:
    num = int(input('Digite um número: '))
    nums.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        spar.append(num)
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        print('-='*50)
        print(f'A lista completa é {nums}')
        print(f'A lista dos pares é {par}')
        print(f'A lista dos impares é {spar}')
        break



