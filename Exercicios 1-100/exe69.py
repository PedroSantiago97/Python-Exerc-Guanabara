listanome = []
listaidade = []
listasexo = []

while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    nome = input('Nome: ')
    idade = input('Idade: ')
    sexo = input('Sexo: [M/F] ')
    print('-'*30)
    op = str(input('Quer continuar? [S/N] '))
    listanome.append(nome)
    listaidade.append(idade)
    listasexo.append(sexo)

    if op.upper() != 'S':
        break

    
print(listaidade)
print(listasexo)
print(listanome)



    



