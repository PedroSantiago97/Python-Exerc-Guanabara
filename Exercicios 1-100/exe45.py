import random
import time

print('Suas opções: ')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

escolha = int(input('Qual é sua jogada? '))
if 0 < escolha > 2:
    print('Digite uma escolha válida!')
else:
    if escolha == 0:
        filtro = 'PEDRA'
    elif escolha == 1:
        filtro = 'PAPEL'
    elif escolha == 2:
        filtro = 'TESOURA'


    opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
    sorteado = random.choice(opcoes)
    print('JO')
    time.sleep(0.8)
    print('KEN')
    time.sleep(0.8)
    print('PO!')
    time.sleep(2)
    print('=-'*15)
    print(f'Jogador escolheu: {filtro}')
    print(f'Computador escolheu {sorteado}')
    print('=-'*15)
    time.sleep(1)


    if sorteado == 'PEDRA' and escolha == 2:
        print('Computador Vence!')
    elif sorteado == 'PAPEL' and escolha == 0:
        print('Computador Vence!')
    elif sorteado == 'TESOURA' and escolha == 1:  
        print('Computador Vence!')
    elif sorteado == filtro:
        print('Deu empate!')
    else:
        print('Você ganhou parabens!')



# , 'PAPEL', 'TESOURA'










