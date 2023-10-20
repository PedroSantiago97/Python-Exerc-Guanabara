import random
num = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))
print('Os valores sorteados são: ', end='')
for c in num:
    print(f'{c} ', end='')
print(f'\nO maior valor foi: {max(num)}')
print(f'O menor valor foi: {min(num)}')
