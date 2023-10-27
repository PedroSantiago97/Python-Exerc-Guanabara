times = ('Botafogo','Bragantino','Grêmio',
'Palmeiras','Flamengo','Fortaleza','Fluminense',
'Athletico-PR','Atlético-MG','São Paulo','Cuiabá',
'Internacional','Cruzeiro','Corinthians','Santos',
'Bahia','Vasco','Goiás','Coritiba',
'América-MG')



print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os cinco primeiros são: {times[:5]}')
print('-='*15)
print(f'Os quatro últimos são: {times[16:]}')
print('-='*15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-='*15)
print(f'O Palmeiras está em {(times.index("Palmeiras")+1)}º lugar!')

i = input('')