
maiorlist = []
menorlist = []
nums = []

for c in range(0, 5):
    num = int(input(f'Digite um valor para a posição {c}: '))
    nums.append(num)
    c+=1


print(f'Você digitou os valores {nums}')

print('=-'*35)

for i in range(0, len(nums)):
    if nums[i] == max(nums):
        maiorlist.append(i)
print(f'O maior valor digitado foi {max(nums)} nas posições ', end='')
for t in maiorlist:
    print(f'{t}...', end='')

for i in range(0, len(nums)):
    if nums[i] == min(nums):
        menorlist.append(i)
print(f'\nO maior valor digitado foi {min(nums)} nas posições ', end='')
for t in menorlist:
    print(f'{t}...', end='')









