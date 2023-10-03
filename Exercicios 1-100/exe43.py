peso = float(input('Qual é seu peso? (Kg) '))
alt = float(input('Qual é seu altura? (m) '))
imc = peso / alt**2


print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc >= 18.5 and imc <= 25:
    print('Parabéns! Você está no peso ideal!')
else:
    if imc < 18.5:
        sit = 'Abaixo do peso normal!'
    elif imc > 25:
        sit = 'com SOBREPESO!'
    elif imc > 30:
        sit = 'em OBSIDADE!'
    elif imc > 40:
        'em OBESIDADE MÓRBIDA, cuidado!'
    print(f'Você está {sit}')
    