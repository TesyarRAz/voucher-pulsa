from model.user import User

class Voucher:
    id: int
    code: str
    saldo: int
    used_by: User = None

    def used_by_name(self):
        return self.used_by.name if self.used_by != None else '-'