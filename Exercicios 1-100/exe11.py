
lar = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

print(f"Sua parede tem a dimensão de {lar} x {alt} e sua aréa é de {(lar*alt):.3f}m².")
print(f"Para pinntar essa parede, você precisará de {((lar*alt)/2):.4f}L de tinta.")

# Poderia colocar tbm print(''.format())
