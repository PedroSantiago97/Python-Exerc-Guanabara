print('========== LOJAS GUANABIRA ===========')
price = float(input('Preço das comprar: R$'))

print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque ')
print('[2] à vista cartão')
print('[3] 2x no cartão') 
print('[4] 3x ou mais no cartão')
option = int(input('Digite a opção desejada? '))
if option == 4:
    par = int(input('Quantas parcelas? '))
elif option == 3:
    par = 2

if option == 1:
    desc = 0.90
    print(f'Sua compra de R${price:.2f} vai custar R${(price*desc):.2f}')

elif option == 2:
    desc = 0.95
    print(f'Sua compra de R${price:.2f} vai custar R${(price*desc):.2f}')
elif option == 3:
    desc = 1
    cond = 'SEM JUROS'
    print(f'Sua compra será parcelada em {par}x de R${((price*desc)/par):.2f} {cond}.')
    print(f'Sua compra de R${price:.2f} vai custar R${(price*desc):.2f} no final.')
elif option == 4:
    desc = 1.2
    cond = 'COM JUROS'
    print(f'Sua compra será parcelada em {par}x de R${((price*desc)/par):.2f} {cond}.')
    print(f'Sua compra de R${price:.2f} vai custar R${(price*desc):.2f} no final.')



