lista = ('Lapis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.30,
         'Canetas', 22.30,
         'Livro', 34.90)
print('_'*45)

print('\n           LISTAGEM DE PREÇOS')
print('_'*45)
print('')
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30} ', end='')
        
    else:
        print(f'R$ {lista[c]:>7.2f}')
print('_'*45)
        
