import random

print('=-'*20)
print('       VAMOS JOGAR PAR OU ÍMPAR !')


while True:
    print('=-'*20)
    numero_aleatorio = random.randint(0, 10)
    valor = int(input('Digite um valor: '))
    op = input('Par ou Impar? [P/I]: ')
    resultado = int(valor + numero_aleatorio)
    print('-'*20)
    print(f'Você jogou {valor} e o computador {numero_aleatorio}. Total de {valor+numero_aleatorio}, deu {par_ou_impar}')
    print('-'*20)
    
   
      







