from typing import List
from model import User
from repository import UserRepository

class UserService:
    repository: UserRepository

    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def findByRole(self, role: str) -> List[User]:
        return self.repository.findByRole(role)

    def findByKode(self, kode: int) -> User:
        return self.repository.findByKode(kode)

    def login(self, username: str, password: str) -> User:
        return self.repository.findByIdentifier(username, password)

    def create(self, user: User):
        self.repository.create(user)

    def update(self, user: User):
        self.repository.update(user)

    def delete(self, user: User):
        self.repository.delete(user)

    def save(self):
        self.repository.save()