from typing import List
from model import PaketData
from repository import PaketDataRepository

class PaketDataService:
    repository: PaketDataRepository

    def __init__(self, repository: PaketDataRepository) -> None:
        self.repository = repository

    def findAll(self) -> List[PaketData]:
        return self.repository.findAll()

    def findByKode(self, kode: str) -> PaketData:
        return self.repository.findByKode(kode)

    def findByJenis(self, role: str) -> List[PaketData]:
        return self.repository.findByJenis(role)

    def create(self, user: PaketData):
        self.repository.create(user)

    def delete(self, user: PaketData):
        self.repository.delete(user)

    def save(self):
        self.repository.save()