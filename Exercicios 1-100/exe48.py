soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'A soma de todos os {contador} valores é {soma}')  



# Exercicio de estruturas de reptições, explorando o aprendizado
# range(): Propriedade que permite a exploração entre valores. (Inicio da contagem, final da contagem, pulos na contagem)
# nos Pulos da contagem, o numero inserido avança entre os valores contados Ex: (0, 10, 2) == 0, 3, 5, 7, 9.
# O exercicio pediu pra contar: Os números impares e divisiveis por 3.
# Contando ainda com um contador para saber quantos termos  foram somados
#  

