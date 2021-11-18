from app import App
import os
from model import User, Voucher
import shutil
import textwrap
import pandas as pd
import tabulate

from service import UserService, VoucherService

class Console(App):
    user: User = None
    userService: UserService = None
    voucherService: VoucherService = None

    def __init__(self, userService: UserService, voucherService: VoucherService) -> None:
        super().__init__()
        self.userService = userService
        self.voucherService = voucherService
    
    def menu(self) -> bool:
        self.header()

        if self.user.role == 'admin':
            return self.menu_admin()
        elif self.user.role == 'user':
            return self.menu_user()

    def menu_admin(self) -> bool:
        self.text_dedent('''
        1. Master User
        2. Master Saldo
        3. Master Produk
        4. Master Paket Data
        5. Riwayat Pembelian
        ''')
        code = self.request()

        if code == 1:
            clear = True
            while True:
                if clear:
                    self.clear()
                    self.header()
                self.text_dedent('''
                1. Daftar User
                2. Tambah User
                3. Edit User
                4. Hapus User
                0. Kembali
                ''')

                clear = True

                code = self.request()
                if code == 1:
                    users = self.userService.findByRole('user')

                    df = pd.DataFrame([(x.kode_user(), x.name, x.username, x.password, x.saldo) for x in users], columns=('ID', 'Nama', 'Username', 'Password', 'Saldo'))

                    df.set_index('ID')

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    clear = False
                elif code == 2:
                    user = User()
                    user.name     = input('Masukan Nama     : ')
                    user.username = input('Masukan Username : ')
                    user.password = input('Masukan Password : ')
                    user.saldo    = 0
                    user.role     = 'user'

                    self.userService.create(user)
                elif code == 3:
                    id = input('ID User [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    user = self.userService.findByKode(id)

                    if user == None:
                        print('User itu tidak ada')
                        input()
                    
                    user.name     = input('Masukan Nama     : ')
                    user.username = input('Masukan Username : ')
                    user.password = input('Masukan Password : ')

                    self.userService.save()

                elif code == 4:
                    id = input('ID User [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    user = self.userService.findByKode(id)

                    if user == None:
                        print('User itu tidak ada')
                        input()
                    
                    self.userService.delete(user)

                elif code == 0:
                    return True
        elif code == 2:
            clear = True
            while True:
                if clear:
                    self.clear()
                    self.header()
                self.text_dedent('''
                1. Daftar Voucher
                2. Tambah Voucher
                3. Hapus Voucher
                0. Kembali
                ''')

                clear = True

                code = self.request()
                if code == 1:
                    vouchers = self.voucherService.findAll()

                    df = pd.DataFrame([(x.code, x.saldo, x.used_by_name()) for x in vouchers], columns=('Code', 'Saldo', 'Dipakai'))

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    clear = False

                elif code == 2:
                    saldo = int(input('Saldo [-1 untuk batal] : '))

                    if saldo == -1:
                        continue

                    voucher = Voucher()
                    voucher.saldo = saldo

                    self.voucherService.create(voucher)

                elif code == 3:
                    id = input('Code Voucher [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    voucher = self.voucherService.findByCode(id)

                    if voucher == None:
                        print('Voucher itu tidak ada')
                        input()
                    
                    self.voucherService.delete(voucher)
                elif code == 0:
                    return True
        elif code == 3:
            clear = True
            while True:
                if clear:
                    self.clear()
                    self.header()
                self.text_dedent('''
                1. Daftar Pulsa
                2. Tambah Pulsa
                3. Edit Pulsa
                4. Hapus Pulsa
                0. Kembali
                ''')

                clear = True

                code = self.request()
                if code == 1:
                    users = self.userService.findByRole('user')

                    df = pd.DataFrame([(x.kode_user(), x.name, x.username, x.password, x.saldo) for x in users], columns=('ID', 'Nama', 'Username', 'Password', 'Saldo'))

                    df.set_index('ID')

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    clear = False
                elif code == 2:
                    user = User()
                    user.name     = input('Masukan Nama     : ')
                    user.username = input('Masukan Username : ')
                    user.password = input('Masukan Password : ')
                    user.saldo    = 0
                    user.role     = 'user'

                    self.userService.create(user)
                elif code == 3:
                    id = input('ID User [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    user = self.userService.findByKode(id)

                    if user == None:
                        print('User itu tidak ada')
                        input()
                    
                    user.name     = input('Masukan Nama     : ')
                    user.username = input('Masukan Username : ')
                    user.password = input('Masukan Password : ')

                    self.userService.save()

                elif code == 4:
                    id = input('ID User [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    user = self.userService.findByKode(id)

                    if user == None:
                        print('User itu tidak ada')
                        input()
                    
                    self.userService.delete(user)

                elif code == 0:
                    return True
        return False

    def menu_user(self) -> bool:
        self.text_dedent('''
        1. Buat Pembelian
        2. Isi Saldo
        3. Riwayat Pembelian
        ''')
        code = self.request()

        if code == 1:
            self.text_dedent('''
            1. Pulsa
            2. Paket Data
            ''')

        return False

    def login(self) -> None:
        self.text_divider('-')
        self.text_center('Login SiPulsa')
        self.text_divider('-')

        username = input('Username : ')
        password = input('Password : ')

        user = self.userService.login(username, password)

        if user == None:
            print('Username atau password salah')
            input()

        self.user = user

    def run(self) -> None:
        while True:
            self.clear()

            if self.user == None:
                self.login()
                continue

            if self.menu():
                continue

            if self.request_lanjut():
                break

    def request(self) -> int:
        return int(input('Masukan Pilihan Anda : '))

    def request_lanjut(self) -> bool:
        return input('Ingin lanjut[Y/n] : ').lower() == 'n'

    def header(self) -> None:
        self.text_divider('-')
        self.text_center('Selamat datang di SiPulsa')
        self.text_divider('-')
        print("Nama  : ", self.user.name)
        print("Saldo : ", 'Unlimited' if self.user.role == 'admin' else '{:n}'.format(self.user.saldo))
        self.text_divider('=')

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

    def text_dedent(self, text: str):
        print(textwrap.dedent(text))