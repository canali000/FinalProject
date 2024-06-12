class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi


    def get_hasta_no(self):
        return self.__hasta_no
    
    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    
    def get_hastalik(self):
        return self.__hastalik
    
    def get_tedavi(self):
        return self.__tedavi

    def set_hasta_no(self,new):
        self.__hasta_no = new
    
    def set_ad(self,new):
        self.__ad = new
    
    def set_soyad(self,new):
        self.__soyad = new
    
    def set_dogum_tarihi(self,new):
        self.__dogum_tarihi = new
    
    def set_hastalik(self,new):
        self.__hastalik = new
    
    def set_tedavi(self,new):
        self.__tedavi = new
    
    def __str__(self):
        return f"Hasta No: {self.__hasta_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Doğum Tarihi: {self.__dogum_tarihi}, Hastalık: {self.__hastalik}, Tedavi: {self.__tedavi}"

    def tedavi_suresi_hesapla(self):
        MIN = 3
        tedavi_suresi = len(self.get_hastalik())

        if tedavi_suresi > 10:
            tedavi_suresi = MIN

        if self.get_tedavi().lower() == "özel tedavi":
            tedavi_suresi += 5

        return tedavi_suresi
