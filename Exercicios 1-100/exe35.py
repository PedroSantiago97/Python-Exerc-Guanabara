print('-='*20)
print('Analisador de Triângulos')
print('-='*20)

ps = float(input('Primeiro segmento: '))
ss = float(input('Segundo segmento: '))
ts = float(input('Terceiro segmento: '))

if ps + ss > ts or ss + ts > ps or ts + ps > ss:
    print('Os segmentos PODEM formar um triangulo')    
else:
    print('Os segmentos NÃO PODEM formar um triangulo')

# Exemplo de condicional com or
# Nessa logica, nao posso ter um triangulo se dois dos segmentos somados nao forem maior que o segmento que resta
# Ex: Primeiro segmento + Terceiro segmento forem Menor que o Segundo segmento

