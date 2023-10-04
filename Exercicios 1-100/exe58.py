import time
import random


print('Oi, Sou seu computador...')
time.sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
time.sleep(1.5)
print('Sera que você consegue advinhar qual foi?')
time.sleep(1)
palp = input('Qual é seu palpite? ')
sorteio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteado = random.choice(sorteio)
contador = 1
while int(palp) != sorteado:
    if int(palp) > sorteado:
        valor = 'Menos'
    else:
        valor = 'Mais'
    print(f'{valor}... Tente mais uma vez')
    palp = input('Qual é seu palpite? ')
    contador += 1
print(f'Acertou com {contador} tentativas. Parabéns !')


