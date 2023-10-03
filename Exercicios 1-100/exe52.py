from colorama import Fore, Back, Style, init
init()
num = int(input('Digite um número: '))
contador = 0
for c in range(1, num+1):
    if num % c == 0:
        cor = Fore.GREEN
        contador += 1
    else:
        cor = Fore.RED
    print(f'{cor}{c}{Style.RESET_ALL}', end=' ')
print()
print(f'O número {num} foi divisível {contador} vezes')
if contador == 2:
    print('E por isso ele é um número PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')



    
 
   

