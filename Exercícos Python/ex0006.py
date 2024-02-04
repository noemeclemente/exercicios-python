# Pintando parede

larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
area = larg * alt
print("Sua parede tem as dimensões de {} X {} e sua área é de {}m".format(larg, alt, area))
tinta = area / 2
print("Para pintar sua parede, você precisará de {} litros de tinta".format(tinta))