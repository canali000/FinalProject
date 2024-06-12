class Personel:
    def __init__(self, personel_no, ad, soyad, departman, maas):
        self.__personel_no = personel_no
        self.__ad = ad
        self.__soyad = soyad
        self.__departman = departman
        self.__maas = maas

    def get_personel_no(self):
        return self.__personel_no 
    
    def get_ad(self):
        return self.__ad 
    
    def get_soyad(self):
        return self.__soyad 
    
    def get_departman(self):
        return self.__departman 
    
    def get_maas(self):
        return self.__maas 
    
    def set_personel_no(self,new):
        self.__personel_no = new 
    
    def set_ad(self,new):
        self.__ad = new
    
    def set_soyad(self,new):
        self.__soyad = new 
    
    def set_departman(self,new):
        self.__departman = new
    
    def set_maas(self,new):
        self.__maas = new
    
    def __str__(self):
        return f"Personel No: {self.__personel_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Departman: {self.__departman}, Maaş: {self.__maas}"
