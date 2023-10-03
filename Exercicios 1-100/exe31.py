from colorama import Fore, Back, Style, init
init()
dis = float(input(f'{Fore.MAGENTA}Digite a distância da viagem em Km: {Style.RESET_ALL}'))

print(f'{Fore.CYAN}Você está prestes a começar uma viagem de {dis:.1f}Km{Style.RESET_ALL}')

if dis < 200:
    print(f'{Fore.YELLOW}E o preço da sua passagem será de R${dis*0.50:.2f}{Style.RESET_ALL}')
else: 
    print(f'{Fore.GREEN
             }E o preço da sua passagem será de R${dis*0.45:.2f}{Style.RESET_ALL}')
