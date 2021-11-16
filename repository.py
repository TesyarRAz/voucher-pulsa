from typing import List
from model import User

from storage import Storage

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
        self.users.append(user)

    def findByIdentifier(self, username: str, password: str) -> User:
        result = [x for x in self.users if x.username == username and password == password]

        if len(result) == 0:
            return None

        return result[0]

    def onInitialize(self):
        admin = User()

        admin.name = 'admin'
        admin.username = 'admin'
        admin.password = 'admin'
        admin.saldo = -1
        admin.role = 'admin'

        self.users.append(admin)

    def onLoad(self):
        self.users = self.storage.data['users']

    def onSave(self):
        self.storage.data['users'] = self.users