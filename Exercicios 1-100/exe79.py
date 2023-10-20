
nums = []
while True:
    num = int(input('Digite um valor: '))
    if num in nums:
        print('Valor duplicado! Não vou adicionar...')
    else:
        nums.append(num)
    op = input('Quer continuar? [S/N]')
    if op in 'nN':
        break
print('-='*50)
print(f'Você digitou os valores {nums}')


    
    

