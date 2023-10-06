c = 0
t = 0
num = 0
lista = []
while c != 999:
    if num != 999:
        num = int(input('Digite um número [999 para parar]: '))
        lista.append(num)
        t += 1
    elif num == 999:
        c = 999
        lista.pop()

print(f'Você digitou {t} números e a soma entre eles foi {sum(lista)}')



    

    


