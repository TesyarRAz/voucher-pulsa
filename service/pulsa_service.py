from typing import List
from model import Pulsa
from repository import PulsaRepository

class PulsaService:
    repository: PulsaRepository

    def __init__(self, repository: PulsaRepository) -> None:
        self.repository = repository

    def findAll(self) -> List[Pulsa]:
        return self.repository.findAll()

    def findByKode(self, kode: int) -> Pulsa:
        return self.repository.findByKode(kode)

    def findByJenis(self, jenis: str) -> List[Pulsa]:
        return self.repository.findByJenis(jenis)

    def create(self, user: Pulsa):
        self.repository.create(user)

    def delete(self, user: Pulsa):
        self.repository.delete(user)

    def save(self):
        self.repository.save()