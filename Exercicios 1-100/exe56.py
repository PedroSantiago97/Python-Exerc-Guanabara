from colorama import Fore, Back, Style, init
init()

listanome = []
listaidade = []
listasexo = []

for c in range(1, 5):
    print(f'----- {c}º PESSOA -----')
    nome = input('Nome: ')
    listanome += [nome]
    idade = input('Idade: ')
    listaidade += [idade]
    sexo = input('Sexo [M/F]: ')
    listasexo += [sexo]

soma = 0   
for c in listaidade:
    soma += int(c)

media = soma/4

listaidadem = []
for c in range(0, 4):
    if listasexo[c].upper() == 'M':
        listaidadem.append(listaidade[c])


for c in range(0, 4):
    if listaidade[c] == max(listaidadem):
        posidade = c

nomemaisv = listanome[posidade]

listaidadef = []
for c in range(0, 4):
    if listasexo[c].upper() == 'F':
        listaidadef.append(listaidade[c])
contadorf = 0
for c in range(0, len(listaidadef)):
    if int(listaidadef[c]) < 20:
        contadorf += 1 


print(f'A média de idade do grupo é de {Fore.GREEN}{media:.1f}{Style.RESET_ALL} anos.')
print(f'O homem mais velho tem {Fore.GREEN}{max(listaidadem)}{Style.RESET_ALL} e se chama {Fore.GREEN}{nomemaisv}{Style.RESET_ALL}.')
print(f'Ao todo são {Fore.GREEN}{contadorf}{Style.RESET_ALL} mulheres com menos de 20 anos.')
input(' ')


