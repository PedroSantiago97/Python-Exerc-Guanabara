soma = 0
contadori = 0
contadorp = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        contadorp += 1
    else:
        contadori += 1

print(f'Existe {contadorp} números pares e {contadori} números impares.')
print(f'A soma dos pares é {soma}.')



