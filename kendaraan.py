class Kendaraan:
    def __init__(self, tipe, plat, merk):
        self.tipe = tipe
        self.plat = plat
        self.merk = merk


kendaraan1 = Kendaraan("Mobil","BM 2268 AA", "Honda")

print(kendaraan1.plat)