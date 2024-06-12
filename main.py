from Hasta import Hasta
from Doktor import Doktor
from Hemsire import Hemsire
from Personel import Personel

staff1 = Personel(1001, "Can Ali", "Bilgin", "Yazılım", 7000000)
staff2 = Personel(1002, "Zeynep", "Kaya", "Muhasebe", 1000)
print(staff1)
print(staff2)
print()

doc1 = Doktor(2001, "Ali", "Ceylan", "Göz", 50000, "Kornea", 5, "Çam Sakura Hastanesi")
doc2 = Doktor(2002, "Mehmet", "Yıldız", "Ortopedi", 18000, "Ortopedi Cerrahisi", 8, "Akdeniz Şehir Hastanesi")
doc3 = Doktor(2003, "Deniz", "Öztürk", "Kardiyoloji", 1000, "Kardiyovasküler Hastalıklar", 10, "Özel Akademi Hastanesi")
print(doc1)
print(doc2)
print(doc3)
print()

nurse1 = Hemsire(3001, "Defne", "Çetin", "Acil Servis", 1000, 40, "İleri Yaşam Desteği", "Beyazgül Hastanesi")
nurse2 = Hemsire(3002, "Melis", "Yılmaz", "Yoğun Bakım", 1000, 35, "Acil Durum Müdahale", "Akdeniz Sağlık Merkezi")
nurse3 = Hemsire(3003, "Burcu", "Demir", "Doğum ve Kadın Hastalıkları", 1000, 30, "Yenidoğan Bakımı", "Elmas Tıp Merkezi")
print(nurse1)
print(nurse2)
print(nurse3)
print()

patient1 = Hasta(4001, "Deniz", "Arslan", "1992-05-14", "Migren", "Akupunktur")
patient2 = Hasta(4002, "İrem", "Kılıç", "1988-08-23", "Epilepsi", "Özel Tedavi")
patient3 = Hasta(4003, "Defne", "Aydın", "1995-03-30", "Diyabet", "İnsülin")

print(patient1)
print(patient2)
print(patient3)
print()

