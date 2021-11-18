from typing import List
from model import Pulsa
from repository import Repository
from storage import Storage

class PulsaRepository(Repository):
    pulsas : List[Pulsa] = []

    def __init__(self, storage: Storage) -> None:
        super().__init__(storage)

    def create(self, user: Pulsa):
        user.id = 1 if len(self.pulsas) == 0 else self.pulsas[-1].id + 1

        self.pulsas.append(user)

        self.save()

    def delete(self, user: Pulsa):
        for i, x in enumerate(self.pulsas):
            if x.id == user.id:
                del self.pulsas[i]

        self.save()

    def findAll(self) -> List[Pulsa]:
        return self.pulsas

    def findByKode(self, kode: int) -> Pulsa:
        return [x for x in self.pulsas if x.kode_pulsa() == kode][0]

    def findByJenis(self, jenis: str) -> List[Pulsa]:
        return [x for x in self.pulsas if x.jenis == jenis]

    def allJenis(self) -> List[str]:
        return list(set([x.jenis for x in self.pulsas]))
    
    def onLoad(self):
        self.pulsas = self.storage.data['pulsas']

    def onSave(self):
        self.storage.data['pulsas'] = self.pulsas