print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)



termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3
print(f'{t1} → {t2} → ', end='')
while c <= termos:
    t3 = t1 + t2
    print(f'{t3} → ', end='')
    t1 = t2
    t2 = t3   
    c += 1

print('FIM')
