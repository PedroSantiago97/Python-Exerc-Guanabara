ano = int(input('Digite o ano que quer analisar: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISEXTO')
else:
    print(f'O ano {ano} não é BISEXTO')
