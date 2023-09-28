import random
import time

num = [0, 1, 2, 3, 4, 5]
sorteado = random.choice(num)
print('-='*68)
print('Eu vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*68)

nump = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3) # Atrasa a execução do codigo, valor em segundos
if nump > 5 or nump < 0:
    print('Digite um número válido !')
else:
    if sorteado == nump:
        print('PARABÉNS! Você conseguiu me vencer!')
    else:
        print(f'GANHEI! Eu pensei no número {sorteado} e não no {nump}')


# Condicional Simples, integrando as bibliotecas time e random pra fazer o Delay do "PROCESSANDO" e a escolha aleatória do número
# Condicional modificada para prever erros de resposta do usuário
