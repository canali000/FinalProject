from Hasta import Hasta
from Doktor import Doktor
from Hemsire import Hemsire
from Personel import Personel
import pandas as pd

staff1 = Personel(1001, "Can Ali", "Bilgin", "Personel", 7000000)
staff2 = Personel(1002, "Zeynep", "Kaya", "Personel", 1000)
print(staff1)
print(staff2)
print()

doc1 = Doktor(2001, "Ali", "Ceylan", "Doktor", 50000, "Göz", 5, "Çam Sakura Hastanesi")
doc2 = Doktor(2002, "Mehmet", "Yıldız", "Doktor", 18000, "Ortopedi", 18, "Akdeniz Şehir Hastanesi")
doc3 = Doktor(2003, "Deniz", "Öztürk", "Doktor", 1000, "Kardiyoloji", 10, "Özel Akademi Hastanesi")
print(doc1)
print(doc2)
print(doc3)
print()

nurse1 = Hemsire(3001, "Defne", "Çetin", "Hemşire", 1000, 40, "İleri Yaşam Desteği", "Beyazgül Hastanesi")
nurse2 = Hemsire(3002, "Melis", "Yılmaz", "Hemşire", 1000, 35, "Acil Durum Müdahale", "Akdeniz Sağlık Merkezi")
nurse3 = Hemsire(3003, "Burcu", "Ceylan", "Hemşire", 1000, 30, "Yenidoğan Bakımı", "Elmas Tıp Merkezi")
print(nurse1)
print(nurse2)
print(nurse3)
print()

patient1 = Hasta(4001, "Defne", "Arslan", "1992-05-14", "Migren", "Akupunktur")
patient2 = Hasta(4002, "İrem", "Kılıç", "1988-08-23", "Epilepsi", "Özel Tedavi")
patient3 = Hasta(4003, "Alp", "Aydın", "1995-03-30", "Diyabet", "İnsülin")

print(patient1)
print(patient2)
print(patient3)
print()

ozellikler = [
    "personel_no", "ad", "soyad", "departman", "maas", "uzmanlik",
    "deneyim_yili", "hastane", "calisma_saati", "sertifika",
    "hasta_no", "dogum_tarihi", "hastalik", "tedavi"
]

frame = pd.DataFrame(columns=ozellikler)
people = [staff1, staff2, doc1, doc2, doc3, nurse1, nurse2, nurse3, patient1, patient2, patient3]

for person in people:
    personData = {}
    for ozellik in ozellikler:
        if hasattr(person, f"get_{ozellik}"):
            personData[ozellik] = getattr(person, f'get_{ozellik}')()
        else:
            personData[ozellik] = None
    frame.loc[len(frame)] = personData


# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)

frame = frame.fillna(0)

docFrame = frame[frame['departman'] == 'Doktor']  
docCount = len(docFrame.groupby('uzmanlik'))

expFrame = docFrame[docFrame['deneyim_yili'] > 5]
expCount = len(expFrame)

patFrame = frame[frame['hastalik'] != 0] 

sortFrame = patFrame.sort_values(by='ad')
alpha = sortFrame["ad"].to_list()

patYoung = patFrame[patFrame['dogum_tarihi'] >= '1990']
patCount = len(patYoung)

richFrame = frame[(frame['departman'] == 'Personel') & (frame['maas'] > 7000)]
richStaff = richFrame["ad"].to_list()


print(f"Doktor sayısı: {docCount}")
print(f"5 yıldan fazla deneyimli doktor sayısı: {expCount}")
print(f"Doğum tarihi 1990 ve sonrası olan hastalar: {patCount}")
print(f"Alfabetik sıralanmış hastalar: {", ".join(alpha)}")
print(f"Maaşı 7000 TL üzerinde olan personeller: {", ".join(richStaff)}")
print()

# Var olan DataFrame’den ad, soyad, departman, maas, uzmanlik, deneyim_yili,
# hastalik, tedavi bilgilerini içeren yeni bir DataFrame elde ediniz ve yazdırınız.

newData = {}

for column in frame.columns:
    newData[column] = frame[column].tolist() 

newFrame = pd.DataFrame(newData)

print(newFrame)