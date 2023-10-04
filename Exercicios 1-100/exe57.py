
sex = input('Informe seu sexo: [M/F] ')
while sex not in 'mMfF':
    sex = input('Dados inválidos, Porfavor, infomre seu sexo: ')
print(f'Sexo {sex.upper()} registrado com sucesso! ')

# Estrutura: Laço de repetição While
# Sentença not: Não esta em, Enquanto não, Valor a ser obtido pra mudança de situação
# Sentença in: Incluido em, Contido em
# Essas sentenças podem ser Ultilizadas sozinhas ou em conjunto como mostrado no caso proposto
