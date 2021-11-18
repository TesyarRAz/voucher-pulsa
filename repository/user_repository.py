from typing import List
from model.user import User
from repository import Repository
from storage import Storage

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