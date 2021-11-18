from typing import List
from model import Voucher, User
from repository import VoucherRepository
import random
import string

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

    def transaction(self, voucher: Voucher, user: User):
        user.saldo += voucher.saldo
        voucher.used_by = user

        self.save()

    def delete(self, user: User):
        self.repository.delete(user)
        
    def save(self):
        self.repository.save()

    