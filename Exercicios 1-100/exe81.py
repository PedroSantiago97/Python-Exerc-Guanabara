nums = []

while True:
    num = int(input('Digite um número: '))
    nums.append(num)
    op = input('Quer continuar? [S/N] ')
    if op in 'Nn':
        print('-='*50)
        nums.sort(reverse=True)
        print(f'Você digitou {len(nums)} elementos')
        print(f'Os valores em ordem decrescente são {nums}')
        if 5 in nums:
            print('O valor 5 faz parte da lista!')
        else:
            print('O valor 5 não faz parte desta lista!')



