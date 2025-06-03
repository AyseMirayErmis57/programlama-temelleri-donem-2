toplam=0
ortalamanizgrenci_notlari = []

for i in range(6):
    ogrenci_notlari.append(int(input("not girin:")))

for ogr_not in ogrenci_notlari :
    toplam = toplam + ogr_not

ortalama=toplam/6

print("ortalamaniz:",ortalama)       