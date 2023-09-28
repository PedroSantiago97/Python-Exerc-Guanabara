ano = int(input('Digite o ano que quer analisar: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISEXTO')
else:
    print(f'O ano {ano} não é BISEXTO')


# Condicional referente ao calculo do ano bisexto
# Um ano bisexto tem que ter resto 0 na divisão por 4
# and nao pode ser divisivél por 100
# or precisa ser divisivel por 400
# fonte: https://escolakids.uol.com.br/matematica/calculo-do-ano-bissexto.html