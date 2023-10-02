print('-='*20)
print('Analisador de Triângulos v2.0')
print('-='*20)

ps = float(input('Primeiro segmento: '))
ss = float(input('Segundo segmento: '))
ts = float(input('Terceiro segmento: '))


if ps + ss < ts or ss + ts < ps or ts + ps < ss:
    print('Os segmentos NÃO PODEM formar um triangulo')   
else:
    if ps == ss == ts:
        tipo = 'EQUILÁTERO'
    elif ps == ss or ps == ts or ts == ss:
        tipo = 'ISÓCELES'
    elif ps != ss or ps != ts or ts != ss:
        tipo = 'ESCALENO'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo}!')


