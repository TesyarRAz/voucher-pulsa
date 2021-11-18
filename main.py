from app import App, Console
from repository import UserRepository, VoucherRepository
from service import UserService, VoucherService
from storage import Storage

import locale

if __name__ == '__main__':
    # Initialisasi Aplikasi
    storage = Storage()

    userRepository = UserRepository(storage)
    voucherRepository = VoucherRepository(storage)

    userService = UserService(userRepository)
    voucherService = VoucherService(voucherRepository)

    app: App = Console(
        userService = userService,
        voucherService = voucherService
    )

    # Run Aplikasi
    locale.setlocale(locale.LC_ALL, 'id_ID')

    storage.load()
    app.run()