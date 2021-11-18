class User:
    id: int
    name: str
    username: str
    password: str
    saldo: int
    role: str

    def kode_user(self):
        return 'USR-' + str.zfill(str(self.id), 3)
