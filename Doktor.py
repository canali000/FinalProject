from Personel import Personel

class Doktor(Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def get_uzmanlik(self):
        return self.__uzmanlik
    
    def get_deneyim_yili(self):
        return self.__deneyim_yili
    
    def get_hastane(self):
        return self.__hastane
    
    def set_uzmanlik(self,new):
        self.__uzmanlik = new
    
    def set_deneyim_yili(self,new):
        self.__deneyim_yili = new
    
    def set_hastane(self,new):
        self.__hastane = new
    
    def __str__(self):
        return f"{super().__str__()}, Uzmanlık: {self.__uzmanlik}, Deneyim Yılı: {self.__deneyim_yili}, Hastane: {self.__hastane}"

    def maas_arttir(self,percent):
        new = self.get_maas() * (1 + percent/100)
        new = round(new,2)
        self.set_maas(new)
