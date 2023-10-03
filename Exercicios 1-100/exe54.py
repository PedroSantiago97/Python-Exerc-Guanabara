import datetime

data_atual = datetime.datetime.now().year
contadormaior = 0 
contadormenor = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    if data_atual - ano < 18:
        contadormenor += 1
    else:
        contadormaior += 1
print(f'Ao todo tivermos {contadormaior} pessoas maiores de idade')
print(f'E também tivemos {contadormenor} pessoas menores de idade')




