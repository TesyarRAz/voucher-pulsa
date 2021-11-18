class PaketData:
    id: int
    name: str
    harga: int
    deskripsi: str
    jenis: str

    def kode_paket(self):
        return 'PKD-' + str.zfill(str(self.id), 3)

class Pulsa:
    id: int
    jenis: str
    harga: int
    pulsa: int

    def kode_pulsa(self):
        return 'PLS-' + str.zfill(str(self.id), 3)
