from .produk import Pulsa, PaketData
from .user import User

class PembelianPulsa:
    id: int
    pulsa: Pulsa
    nomor: str
    user: User

class PembelianPaketData:
    id: int
    paket: PaketData
    nomor: str
    user: User
