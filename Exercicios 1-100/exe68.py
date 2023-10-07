import random

print('=-'*20)
print('       VAMOS JOGAR PAR OU ÍMPAR !')

t=0
while True:
    print('=-'*20)
    numero_aleatorio = random.randint(0, 10)
    valor = int(input('Digite um valor: '))
    op = input('Par ou Impar? [P/I]: ')
    resultado = int(valor + numero_aleatorio)
    if resultado % 2 == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'IMPAR'
    print('-'*50)
    print(f'Você jogou {valor} e o computador {numero_aleatorio}. Total de {valor+numero_aleatorio}, deu {parouimpar}')
    print('-'*50)   
    if resultado % 2 == 0 and op.upper() == 'P'or resultado % 2 != 0 and op.upper() == 'I':
        print(f'Você VENCEU!')
        print('Vamos joguar novamente...')
        t+=1
    else:
        print(f'Você PERDEU!')
        print('-'*50) 
        print(f'GAME OVER!, você venceu {t} vezes')
        break
    


    

    
   
      







