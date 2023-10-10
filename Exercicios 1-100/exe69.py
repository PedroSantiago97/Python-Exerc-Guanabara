listanome = []
listaidade = []
listasexo = []
lista18 = []
listam = []
listawo = []
c = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ')
    while sexo not in 'mfMF':
        sexo = str(input('Sexo: [M/F] '))
    print('-'*30)
    op = str(input('Quer continuar? [S/N] '))
    listanome.append(nome)
    listaidade.append(idade)
    listasexo.append(sexo)
    
    if op.upper() != 'S':
        break

for i in range(0, len(listaidade)):
    if listaidade[i] > 18:
        lista18.append(listaidade[i])
    i+=1

for j in range(0, len(listasexo)):
    if listasexo[j].upper() == 'M':
        listam.append(listasexo[j])
    j+=1


for o in range(0, len(listasexo)):
    if listasexo[o].upper() == 'F' and listaidade[o] < 20:
        listawo.append(listasexo[o])
    o+=1


print(f'Total de pessoas com mais de 18 anos: {len(lista18)}')
print(f'Ao todo temos {len(listam)} homens cadastrados')
print(f'E temos {len(listawo)} mulheres com menos de 20 anos')






    



