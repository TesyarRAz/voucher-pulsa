from typing import List, Union
from model import PembelianPulsa, PembelianPaketData
from repository import PembelianRepository

class PembelianService:
    repository: PembelianRepository

    def __init__(self, repository: PembelianRepository) -> None:
        self.repository = repository

    def findAllPulsa(self) -> List[PembelianPulsa]:
        return self.repository.findAllPulsa()

    def findAllPaketData(self) -> List[PembelianPaketData]:
        return self.repository.findAllPaketData()

    def create(self, pembelian: Union[PembelianPulsa, PembelianPaketData]):
        self.repository.create(pembelian)

    def delete(self, pembelian: Union[PembelianPulsa, PembelianPaketData]):
        self.repository.delete(pembelian)

    def save(self):
        self.repository.save()