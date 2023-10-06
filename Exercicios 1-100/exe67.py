c=0
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num >= 0:
        print('-'*15)
        for c in range(0, 11):
            print(f'{num}  X {c:2} = {c*num}')
        print('-'*15)    
    else:
        print('Fim')
        break

