c = 0
t = 0
num = 0
lista = []
while True:
    if num != 999:
        num = int(input('Digite um número (999 para parar): '))
        lista.append(num)
        t += 1
    elif num == 999:
        lista.pop()
        break

print(f'Você digitou {t} números e a soma entre eles foi {sum(lista)}')


