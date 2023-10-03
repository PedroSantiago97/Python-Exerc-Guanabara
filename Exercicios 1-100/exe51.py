print('='*38)
print('         10 TERMOS DE UMA PA ')
print('='*38)

termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10-1) * razao
for c in range(termo1, decimo, razao):   
    print(c, end=' → ',)
print('ACABOU')

# Pensar na formula da PA
# Olhar a repetição e ter claro o começo e o final dela
# Ter o controle da repetição é saber aonde começa e onde termina !!!!
# an = a1 + (n – 1)r : Formula pra saber qualquer termo, nesse caso, o decimo !!!
    


