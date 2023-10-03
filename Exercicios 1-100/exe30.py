from colorama import Fore, Back, Style, init
init()
num = int(input(f'{Fore.LIGHTMAGENTA_EX}Me diga um número qualquer: {Style.RESET_ALL}'))

if num % 2 != 0:
    print(f'O número {num} é {Fore.BLUE}ÍMPAR{Style.RESET_ALL}')
else: 

    print(f'O número {num} é {Fore.GREEN}PAR{Style.RESET_ALL}')
    
