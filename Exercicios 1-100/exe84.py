nomes = []
dado = []
pesomlist = []
pesominlist = []
pesom = 0
pesomen = float('inf')

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    nomes.append(dado[:])
    dado.clear()
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        break

print('-='*50)

print(f'Ao todo você cadastrou {len(nomes)} pessoas.')
for c, i in nomes:
    if i > pesom:
        pesom = i
print(f'O maior peso foi {pesom:.2f} Kg. ', end='')
for c, i in nomes:
    if i == pesom:
        pesomlist.append(c)
print(f'Peso de {pesomlist}')

for c, i in nomes:
    if i < pesomen:
        pesomen = i
print(f'O menor peso foi {pesomen:.2f} Kg. ', end='')
for c, i in nomes:
    if i == pesomen:
        pesominlist.append(c)
print(f'Peso de {pesominlist}')



