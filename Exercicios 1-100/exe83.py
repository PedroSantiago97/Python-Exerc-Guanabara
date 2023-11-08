
exp = input('Digite sua expressão: ')
annex = []
for c in exp:
    annex.append(c)

paren = []
for i in annex:
    if i in '()':
        paren.append(i)

cont1 = 0
cont2 = 0
for c in paren:
    if c == '(':
        cont1 += 1
    else:
        cont2 += 1


if cont1 == cont2:
    print('Sua expressão esta válida!')
else:
    print('Sua expressão esta errada !')








