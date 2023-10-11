print('='*30)
print('          BANCO CEV')
print('='*30)

sac = int(input('Que valor você quer sacar? R$'))
total = sac
cédulas =           [50, 20, 10, 1]
quantidade_cédulas =[ 0,  0,  0, 0]
# Foram declaradas: Valor de saque = sac, Lista de cedulas = cédulas e a Qtd de cedulas = quantidade_cédulas

# A primeira repetição vai dizer quantas cedulas de cada irei precisar
# de acordo a posição dela na lista
# Ex: [50, 20, 10, 1] 
#     [2 ,  1,  0, 0] se o valor for 120
for i in range(len(cédulas)):
    # Na primeira parte da identação, a variável i que sera igual a 0 ira percorrer
    # a lista de cédulas afim de dividir o valor de saque e descobrir
    # a quantidade de cedulas que irei precisar

    # Ex: se o sque for 1531, como o primeiro valor de cédulas[i] é 50
    # logo 1531 será dividido, *nesse caso só o inteiro*, por 50 e 
    # em seguida o valor 30 sera inserido em quantidade_cédulas[i]
    quantidade_cédulas[i] = total // cédulas[i]

    # Na segunda parte da indentação, o total do saque é posto em resto com 
    # a cédula que foi ultilizada anteriormente, no caso, 50
    # isso serve pra descobrir o valor, que consequentemente será
    # menor que 50, portanto impossivel de continuar a divisão de cédulas

    # Ex: se o saque for de 1531, tera como resto dessa operação o valor de 31
    # pois 1531/50 nao é uma divisão exata, portanto, o resto é o valor 
    # que se retirado a divisão sera exata
    total %= cédulas[i]

for i in range(len(cédulas)):
    # A segunda estrutura de repetição vai imprimir esses valores
    # Sendo condicionados a imprimir se o valor de quantidade de cedulas for maior que 0
    if quantidade_cédulas[i] > 0:
        print(f'Total de {quantidade_cédulas[i]} cédula(s) de R${cédulas[i]}')

print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

    

    

    


     
         
