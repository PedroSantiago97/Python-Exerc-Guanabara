from colorama import Fore, Back, Style, init
init()
vel = int(input(f'{Fore.BLUE}Qual a velocidade atual do carro? {Style.RESET_ALL}'))

if vel >= 80:
    print(f'{Fore.RED}MULTADO! Você excedeu o limite permitido que é de 80 Km/h{Style.RESET_ALL}')
    print(f'{Fore.RED}Você deve pagar uma multa de R${((vel-80)*7)+120}{Style.RESET_ALL}')
    print(f'{Fore.GREEN}Tenha um bom dia! Dirija com segurança!{Style.RESET_ALL}')
else:
    print(f'{Fore.GREEN}Tenha um bom dia! Dirija com segurança!{Style.RESET_ALL}')
    
# Condicional Simples
# Porém com resalvas da biblioteca colorama, que tingiu o codigo
# importa digitando no codigo: from colorama import Fore, Back, Style, init
# coloca-se {Fore.RED} {Fore.GREEN} {Fore.BLUE} Na frente do texto e {Style.RESET_ALL} no final do texto mas tudo dentro das aspas

# Segue o exemplo : print(f'{Fore.BLUE} Meu texto {Style.RESET_ALL}')
