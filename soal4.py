class Buah :
    def __init__(self,Nama,Warna,Rasa):
        self.Nama = Nama
        self.Warna = Warna
        self.Rasa = Rasa

    def setNama(self,Nama):
        self.Nama = Nama

    def setWarna(self,Warna):
        self.Warna = Warna

    def setRasa(self,Rasa):
        self.Rasa = Rasa

    def get_informasi(self):
        return f'Nama Buah : {self.Nama}\nWarna Buah : {self.Warna}\nRasa  : {self.Rasa}'


class Manga(Buah):
    def __init__(self, Nama, Warna, Rasa,Vitamin):
        super().__init__(Nama,Warna,Rasa)
        self.Vitamin = Vitamin
    def setVitamin(self,Vitamin):
        self.Vitamin = Vitamin

    def informasi(self):
        return f'{super().get_informasi()}\nVitamin : {self.Vitamin}'
buahh = Manga('Apel','Merah','Manis','B')
print(buahh.informasi())



    

    

    
