pr = float(input('Primeira nota: '))
sg = float(input('Segunda nota: '))

media = (pr + sg) / 2
print(f'Tirando {pr} e {sg}, a média do aluno é {media:.1f}')
if media > 6:  
    print('O aluno está APROVADO!')
elif media <= 6.9 and media >= 5.0:   
    print('O aluno está de RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está REPROVADO!')

# Um adeno a produção de codigo limpo
# Se houver necessidade de repetir o codigo nao precisa colocar no if !!!!