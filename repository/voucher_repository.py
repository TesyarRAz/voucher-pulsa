from typing import List
from model import Voucher
from repository import Repository
from storage import Storage

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