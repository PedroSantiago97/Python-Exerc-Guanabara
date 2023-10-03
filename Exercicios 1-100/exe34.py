sal = float(input('Qual é o salário do funcionario? R$'))

if sal >= 1250:
    saln = sal*1.10
else:
    saln = sal*1.15

print(f'O salário do funcionário, com o aumento é de: R${saln:.2f}')

# Exercicio que requer um conhecimento matemático sobre porcentagem
# Simples condicional, Mais um so do controlador de termos apos a virgula: :.2f
