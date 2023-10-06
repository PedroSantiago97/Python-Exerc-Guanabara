print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)

c = 0
lista = [0, 1]
termos = int(input('Quantos termos você quer mostrar? '))
print('~'*30)

print(f'{lista[0]} → {lista[1]} → ', end='')

for c in range(2, termos):

    lista.append(lista[c - 1] + lista[c - 2])
    
    print(f'{lista[c]} → ', end='')

print('FIM')  
print('~'*30)

# Exercicio de fibonacci feito com 


