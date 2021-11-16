class User:
    id: int
    name: str
    username: str
    password: str
    saldo: int
    role: str

    def kode_user(self):
        return 'USR-' + str.zfill(str(self.id), 3)

class Voucher:
    id: int
    code: str
    saldo: int
    used_by: User = None

    def used_by_name(self):
        return self.used_by.name if self.used_by != None else '-'

class Pembelian:
    id: int
    pulsa: int
    nomor: str