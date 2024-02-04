# Conversor de medidas

medida = float(input("Uma distância em metros: "))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print("A distância de {}m corresponde a {}cm, a {}mm, a {}km, a {}hm, a {}dam, a {}dm".format(medida, cm, mm, km, hm, dam, dm))