import time
from colorama import Fore, Style, init
init()

casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
pre = int(input('Quantos anos de financiamento: '))

par = pre*12


print(f'Para comprar uma casa de R${casa:.2f} a prestação será de R${casa/par:.2f}')
if casa/par > sal*0.3:
    
    print(f'Emprestimo {Fore.RED}NEGADO{Style.RESET_ALL}')
elif casa/par < sal*0.3:
    
    print(f'Emprestimo {Fore.GREEN}CONCEDIDO{Style.RESET_ALL}')
