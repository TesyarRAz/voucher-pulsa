from cmd.console import Console
from repository import *
from service import *
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

    app = Console(
        userService = userService,
        voucherService = voucherService,
        pulsaService = pulsaService,
        paketDataService = paketDataService,
        pembelianService = pembelianService
    )

    # Run Aplikasi
    # locale.setlocale(locale.LC_ALL, 'id_ID')

    storage.load()
    app.run()