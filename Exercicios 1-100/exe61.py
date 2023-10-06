print('Gerador de PA')
print('-='*10)
pr = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
c = 0
while c < 10:
    print(f'{pr} → ', end='')
    pr += rz
    c += 1
print('FIM', end='')




