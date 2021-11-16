from app import App
from console import Console
from repository import UserRepository
from service import UserService
from storage import Storage

import locale

if __name__ == '__main__':
    # Initialisasi Aplikasi
    storage = Storage()

    userRepository = UserRepository(storage)

    userService = UserService(userRepository)

    app: App = Console(
        userService = userService
    )

    # Run Aplikasi
    locale.setlocale(locale.LC_ALL, 'id_ID')

    storage.load()
    app.run()