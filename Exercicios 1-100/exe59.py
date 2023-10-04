import time

pr = int(input('Primeiro valor: '))
sg = int(input('Segundo valor: '))
po = '1'
go = '1'

while po in go:
    time.sleep(0.5)
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    op = int(input('>>>>> Qual é a sua opção? '))
    time.sleep(0.5)
    if op == 1:
        print(f'A soma entre {pr} + {sg} é {pr+ sg}')
        print('=-='*10)
    elif op == 2:
        print(f'A multiplicação entre {pr} * {sg} é {pr*sg}')
        print('=-='*10)
    elif op == 3:
        if pr > sg:
            result = pr
        else:
            result = sg
        print(f'O maior valor entre {pr} e {sg} é {result}')
        print('=-='*10)
    elif op == 4:
        pr = int(input('Primeiro valor: '))
        sg = int(input('Segundo valor: '))
        print('=-='*10)
    elif op == 5:
        go = '0'
        print('=-='*10)
    else:
        print('Opção inválida, tente novamente: ')
print('Obrigado, Volte sempre!')

       



   





