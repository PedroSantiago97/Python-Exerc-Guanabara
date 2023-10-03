import datetime
import time

anonasc = int(input('Ano de nascimento: '))
ano_atual = datetime.datetime.now().year

print('ANALISANDO...')
time.sleep(0.8)


if (ano_atual - anonasc) < 18:
    print(f'Quem nasceu em {anonasc} tem {ano_atual - anonasc} anos em {ano_atual}. ')
    print(f'Ainda faltam {18 - (ano_atual - anonasc)} anos para o alistamento.')
    print(f'Seu alistamento será em {anonasc + 18}')
elif ano_atual - anonasc > 18:
    print(f'Quem nasceu em {anonasc} tem {ano_atual - anonasc} anos em {ano_atual}. ')
    print(f'Você já deveria ter se alistado a {ano_atual - (anonasc + 18)} anos.')
    print(f'Seu alistamento foi em {anonasc + 18}.')
else:
    print(f'Quem nasceu em {anonasc} tem {ano_atual - anonasc} em {ano_atual}.')
    print('Você tem que se alistar IMEDIATAMENTE!')




