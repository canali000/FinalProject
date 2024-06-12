from Personel import Personel

class Hemsire(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def get_calisma_saati(self):
        return self.__calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def get_hastane(self):
        return self.__hastane

    def set_calisma_saati(self,new):
        self.__calisma_saati = new
    
    def set_sertifika(self,new):
        self.__sertifika = new
    
    def set_hastane(self,new):
        self.__hastane = new

    def __str__(self):
        return f"{super().__str__()}, Çalışma Saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"

    def maas_arttir(self, percent):
        pass
