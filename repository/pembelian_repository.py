from typing import List, Union
from model import PembelianPulsa, PembelianPaketData
from repository import Repository
from storage import Storage

class PembelianRepository(Repository):
    pembelian_pulsas : List[PembelianPulsa] = []
    pembelian_paketdatas: List[PembelianPaketData] = []

    def __init__(self, storage: Storage) -> None:
        super().__init__(storage)

    def create(self, pembelian: Union[PembelianPulsa, PembelianPaketData]):
        if isinstance(pembelian, PembelianPulsa):
            pembelian.id = 1 if len(self.pembelian_pulsas) == 0 else self.pembelian_pulsas[-1].id + 1

            self.pembelian_pulsas.append(pembelian)
        elif isinstance(pembelian, PembelianPaketData):
            pembelian.id = 1 if len(self.pembelian_paketdatas) == 0 else self.pembelian_paketdatas[-1].id + 1

            self.pembelian_paketdatas.append(pembelian)

        self.save()

    def delete(self, pembelian: Union[PembelianPulsa, PembelianPaketData]):
        if isinstance(pembelian, PembelianPulsa):
            for i, x in enumerate(self.pembelian_pulsas):
                if x.id == pembelian.id:
                    del self.pembelian_pulsas[i]
        elif isinstance(pembelian, PembelianPaketData):
            for i, x in enumerate(self.pembelian_paketdatas):
                if x.id == pembelian.id:
                    del self.pembelian_paketdatas[i]

        self.save()

    def findAllPulsa(self) -> List[PembelianPulsa]:
        return self.pembelian_pulsas

    def findAllPaketData(self) -> List[PembelianPaketData]:
        return self.pembelian_paketdatas
    
    def onLoad(self):
        self.pembelian_pulsas = self.storage.data['pembelian_pulsas']
        self.pembelian_paketdatas = self.storage.data['pembelian_paketdatas']

    def onSave(self):
        self.storage.data['pembelian_pulsas'] = self.pembelian_pulsas
        self.storage.data['pembelian_paketdatas'] = self.pembelian_paketdatas