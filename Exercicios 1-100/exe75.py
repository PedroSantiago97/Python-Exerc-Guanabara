num = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
c = 0
i = 0
p = 0
print(f'Você digitou os valores {num}')
for c in range(0, len(num)):
    if num[c] == 9:
        i+=1
        c+=1
    else:
        c+=1
print(f'O número 9 aparece {i} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição!')
else:
    print('O valor 3 não está em nenhuma posição!')
for c in range(0, len(num)):
    if num[c] % 2 == 0:
        p+=1
        c+=1
    else:
        c+=1
print(f'Os valores pares digitados foram {p}')



