pri = int(input('Primeiro valor: '))
seg = int(input('Segundo valor: '))
ter = int(input('Terceiro valor: '))


if pri > seg and pri > ter:
    maior = pri
elif seg > pri and seg > ter:
    maior = seg
else:
    maior = ter

if pri < seg and pri < ter:
    menor = pri
elif seg < pri and seg < ter:
    menor = seg
else:
    menor = ter

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi {maior}')



