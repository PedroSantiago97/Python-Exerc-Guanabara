print('-'*40)
print('           LOJA SUPER BARATAO')
print('-'*40)

listanome = []
listapreco = []
lista1000 = []


while True:
    nome = input('Nome do produto: ')
    price = int(input('Preço: R$'))
    op = str(input('Quer continuar? [S/N] '))

    listanome.append(nome)
    listapreco.append(price)
    if op.lower() == 'n':
       break

for i in range(0, len(listapreco)):
    if listapreco[i] > 1000:
        lista1000.append(listapreco[i])

menor = min(listapreco)
minpos = listapreco.index(menor)

print('----------- FIM DO PROGRAMA ------------')
print(f'O total da compra foi R${sum(listapreco):.2f}')
print(f'Temos o total de {len(lista1000)} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {listanome[minpos]} que custa R${menor} ')

# Função .index()
# Acha a posição de algum valor, colocado entre parenteses, que esteja dentro da lista



