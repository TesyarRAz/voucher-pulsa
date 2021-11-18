from typing import List
from model import PaketData
from repository import Repository
from storage import Storage

class PaketDataRepository(Repository):
    paketdatas : List[PaketData] = []

    def __init__(self, storage: Storage) -> None:
        super().__init__(storage)

    def create(self, user: PaketData):
        user.id = 1 if len(self.paketdatas) == 0 else self.paketdatas[-1].id + 1

        self.paketdatas.append(user)

        self.save()

    def delete(self, user: PaketData):
        for i, x in enumerate(self.paketdatas):
            if x.id == user.id:
                del self.paketdatas[i]

        self.save()

    def findAll(self) -> List[PaketData]:
        return self.paketdatas

    def findByKode(self, kode: int) -> PaketData:
        return [x for x in self.paketdatas if x.kode_paket() == kode][0]

    def findByJenis(self, jenis: str) -> List[PaketData]:
        return [x for x in self.paketdatas if x.jenis == jenis]

    def allJenis(self) -> List[str]:
        return list(set([x.jenis for x in self.paketdatas]))
    
    def onLoad(self):
        self.paketdatas = self.storage.data['paketdatas']

    def onSave(self):
        self.storage.data['paketdatas'] = self.paketdatas