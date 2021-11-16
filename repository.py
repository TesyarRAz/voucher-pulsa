from typing import List
from model import User, Voucher

from storage import Storage
import copy

class Repository:
    storage: Storage = None

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

        self.storage.onInitialize.append(self.onInitialize)
        self.storage.onLoad.append(self.onLoad)
        self.storage.onSave.append(self.onSave)

    def load(self):
        self.storage.load()

    def save(self):
        self.storage.save()

    def onInitialize(self):
        pass

    def onLoad(self):
        pass

    def onSave(self):
        pass

class UserRepository(Repository):
    users : List[User] = []

    def __init__(self, storage: Storage) -> None:
        super().__init__(storage)

    def create(self, user: User):
        user.id = 1 if len(self.users) == 0 else self.users[-1].id + 1

        self.users.append(user)

        self.save()

    def delete(self, user: User):
        for i, x in enumerate(self.users):
            if x.id == user.id:
                del self.users[i]

        self.save()

    def findByRole(self, role: str) -> List[User]:
        return [x for x in self.users if x.role == role]

    def findByKode(self, kode: int) -> User:
        return [x for x in self.users if x.kode_user() == kode][0]

    def findByIdentifier(self, username: str, password: str) -> User:
        result = [x for x in self.users if x.username == username and password == password]

        if len(result) == 0:
            return None

        return result[0]

    def onInitialize(self):
        admin = User()

        admin.name     = 'admin'
        admin.username = 'admin'
        admin.password = 'admin'
        admin.saldo    = -1
        admin.role     = 'admin'

        self.create(admin)

    def onLoad(self):
        self.users = self.storage.data['users']

    def onSave(self):
        self.storage.data['users'] = self.users

class VoucherRepository(Repository):
    vouchers : List[Voucher] = []

    def __init__(self, storage: Storage) -> None:
        super().__init__(storage)

    def create(self, voucher: Voucher):
        voucher.id = 1 if len(self.vouchers) == 0 else self.vouchers[-1].id + 1

        self.vouchers.append(voucher)

        self.save()

    def delete(self, voucher: Voucher):
        for i, x in enumerate(self.vouchers):
            if x.id == voucher.id:
                del self.vouchers[i]

        self.save()

    def findAll(self) -> List[Voucher]:
        return self.vouchers

    def findByCode(self, kode) -> Voucher:
        return [x for x in self.vouchers if x.code == kode][0]


    
    def onLoad(self):
        self.vouchers = self.storage.data['vouchers']

    def onSave(self):
        self.storage.data['vouchers'] = self.vouchers