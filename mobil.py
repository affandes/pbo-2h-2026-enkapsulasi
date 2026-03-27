class Mobil:
    def __init__(self, plat, merk):
        print("Run init in Mobil")
        self.plat = plat
        self.merk = merk

    def get_plat(self):
        return self.plat

class Truk(Mobil):
    def __init__(self, plat, merk, tonase):
        print("Run init in Truk")
        self.tonase = tonase
        super().__init__(plat, merk)


kendaraan1 = Truk("BM 2268 AA", "Honda", 500)

print(kendaraan1.get_plat())