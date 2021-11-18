from cmd import App, Console
from repository import UserRepository, VoucherRepository
from repository.paketdata_repository import PaketDataRepository
from repository.pembelian_repository import PembelianRepository
from repository.pulsa_repository import PulsaRepository
from service import UserService, VoucherService, PulsaService, PaketDataService
from service.pembelian_service import PembelianService
from storage import Storage

import locale

if __name__ == '__main__':
    # Initialisasi Aplikasi
    storage = Storage()

    userRepository = UserRepository(storage)
    voucherRepository = VoucherRepository(storage)
    pulsaRepository = PulsaRepository(storage)
    paketDataRepository = PaketDataRepository(storage)
    pembelianRepository = PembelianRepository(storage)

    userService = UserService(userRepository)
    voucherService = VoucherService(voucherRepository)
    pulsaService = PulsaService(pulsaRepository)
    paketDataService = PaketDataService(paketDataRepository)
    pembelianService = PembelianService(pembelianRepository)

    app: App = Console(
        userService = userService,
        voucherService = voucherService,
        pulsaService = pulsaService,
        paketDataService = paketDataService,
        pembelianService = pembelianService
    )

    # Run Aplikasi
    locale.setlocale(locale.LC_ALL, 'id_ID')

    storage.load()
    app.run()