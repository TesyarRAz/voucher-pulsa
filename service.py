from typing import List
from model import User, Voucher
from repository import UserRepository, VoucherRepository
import random
import string

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

    def delete(self, user: User):
        self.repository.delete(user)

    def save(self):
        self.repository.save()

class VoucherService:
    repository: VoucherRepository

    def __init__(self, repository: VoucherRepository) -> None:
        self.repository = repository

    def findAll(self) -> List[Voucher]:
        return self.repository.findAll()

    def findByCode(self, kode: int) -> Voucher:
        return self.repository.findByCode(kode)

    def create(self, voucher: Voucher):
        voucher.code = ''.join(random.choices(string.digits, k=16))

        self.repository.create(voucher)

    def delete(self, user: User):
        self.repository.delete(user)
        
    def save(self):
        self.repository.save()

    