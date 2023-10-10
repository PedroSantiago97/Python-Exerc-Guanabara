print('='*30)
print('          BANCO CEV')
print('='*30)
sac =  int(input('Que valor você quer sacar? R$'))
total = sac
totced = 0
ced = 50

while True:
    if total >= 50:
        totced += 1
        total -= ced
    else:
        print(f'Total de {totced} cédulas de {ced}')
        break

    

    

    


     
         
