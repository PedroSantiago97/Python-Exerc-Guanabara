num = []
t = 0
for c in range(0, 5):
    op = int(input('Digite um valor: '))
    if c == 0 or op > max(num):
        num.append(op)
        print('Valor adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if op <= num[pos]:
                num.insert(pos, op)
                print(f'Valor adicionado na posição {pos}...')
                break
            pos+=1
print('-='*50)
print(f'Os valores digitados em ordem foram {num}')        


