print('Gerador de PA')
print('-='*10)
pr = int(input(f'Primeiro termo: '))
rz = int(input(f'Razão da PA: '))
c = 0
# Aqui é o calculo normal de PA visto outras vezes e feito com o WHILE dessa vez
while c < 10:
    print(f'{pr} → ', end='')
    pr += rz
    c += 1
    if c == 10:
        print('PAUSA', end='')
# Pra essa estrutura de repetição criei uma variável -1, por que pela logica nao tem como coloca -3 números a mais, logo a variável começa num valimpossivel diante a prerrogativa do exervicicio, fazendo com que ela possa ser substituida com um imput() e dando continuidade ao processo
c2 = -1
tc = 0
# Nessa repetição colocamos outra dentro e apos
while c2 != 0:
    print('')
    c2 = int(input('Quantos termos você quer mostrar a mais? '))
    t = 0
    while t < c2:
        print(f'{pr} → ', end='')
        pr += rz
        t += 1
        tc += 1
        if t == c2:
           print('PAUSA', end='')
    if c2 == 0:
        print(f'Progressão finalizada com {tc+10} termos mostrados!')
        
        
            


    



    






