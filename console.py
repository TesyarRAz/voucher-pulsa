from app import App
import os
from model import User
import shutil

from service import UserService

class Console(App):
    user: User = None
    userService: UserService = None

    def __init__(self, userService: UserService) -> None:
        super().__init__()
        self.userService = userService

    def login(self) -> None:
        self.text_divider('-')
        self.text_center('Login SiPulsa')
        self.text_divider('-')

        username = input('Username : ')
        password = input('Password : ')

        user = self.userService.login(username, password)

        if user == None:
            print('Username atau password salah')

        self.user = user

    def run(self) -> None:
        while True:
            self.clear()

            if self.user == None:
                self.login()
                continue

            self.menu()

            if input('Ingin lanjut[Y/n] : ').lower() == 'n':
                break

    def menu(self) -> None:
        self.text_divider('-')
        self.text_center('Selamat datang di SiPulsa')
        self.text_divider('-')
        print("Nama  : ", self.user.name)
        print("Saldo : {:n}".format(self.user.saldo))
        self.text_divider('=')

        print('''
        1. Isi Pulsa
        2. 
        ''')

    def clear(self) -> None:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def text_center(self, text: str):
        print(text.center(shutil.get_terminal_size().columns))

    def text_divider(self, text: str, size: int = None):
        if size == None:
            size = shutil.get_terminal_size().columns
        
        print(text * size)