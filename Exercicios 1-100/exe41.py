import datetime

anonasc = int(input('Ano de nascimento: '))
data_atual = datetime.datetime.now().year
idade = data_atual - anonasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else: 
    print('Classificação: MASTER')

# Mais um adeno a fazer cogido limpo
# Nao precisa aprisionar a condição, analisar e fazer um codigo mais rapido 

