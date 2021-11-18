from cmd import App
import os
from typing import List
from model import User, Voucher, Pulsa, PaketData, PembelianPulsa, PembelianPaketData
import shutil
import textwrap
import pandas as pd
import tabulate

from service import UserService, VoucherService, PaketDataService, PulsaService, PembelianService

class Console(App):
    user: User = None
    userService: UserService = None
    voucherService: VoucherService = None
    pulsaService: PulsaService = None
    paketDataService: PaketDataService = None
    pembelianService: PembelianService = None

    def __init__(self, 
        userService: UserService, 
        voucherService: VoucherService, 
        pulsaService: PulsaService, 
        paketDataService: PaketDataService, 
        pembelianService: PembelianService) -> None:
        super().__init__()
        self.userService = userService
        self.voucherService = voucherService
        self.pulsaService = pulsaService
        self.paketDataService = paketDataService
        self.pembelianService = pembelianService
    
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
        3. Master Pulsa
        4. Master Paket Data
        5. Riwayat Pembelian
        9. Logout
        0. Keluar
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

                    input('Berhasil tambah data')
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

                    input('Berhasil edit data')

                elif code == 4:
                    id = input('ID User [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    user = self.userService.findByKode(id)

                    if user == None:
                        print('User itu tidak ada')
                        input()
                    
                    self.userService.delete(user)

                    input('Berhasil hapus data')

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

                    input('Berhasil tambah data')

                elif code == 3:
                    id = input('Code Voucher [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    voucher = self.voucherService.findByCode(id)

                    if voucher == None:
                        print('Voucher itu tidak ada')
                        input()
                    
                    self.voucherService.delete(voucher)

                    input('Berhasil hapus data')
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
                    filter = input('Filter berdasarkan jenis [kosongkan jika ingin tampilkan semua] : ')

                    pulsas: List[Pulsa] = None

                    if filter == '':
                        pulsas = self.pulsaService.findAll()
                    else:
                        pulsas = self.pulsaService.findByJenis(filter)

                    df = pd.DataFrame([(x.kode_pulsa(), x.pulsa, x.harga, x.jenis) for x in pulsas], columns=('ID', 'Pulsa', 'Harga', 'Jenis'))

                    df.set_index('ID')

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    clear = False
                elif code == 2:
                    pulsa = Pulsa()
                    pulsa.jenis = input('Masukan Jenis : ')
                    pulsa.pulsa = input('Masukan Pulsa : ')
                    pulsa.harga = int(input('Masukan Harga : '))

                    self.pulsaService.create(pulsa)

                    input('Berhasil tambah data')
                elif code == 3:
                    id = input('ID Pulsa [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    pulsa = self.pulsaService.findByKode(id)

                    if pulsa == None:
                        print('Pulsa itu tidak ada')
                        input()
                    
                    pulsa.jenis = input('Masukan Jenis : ')
                    pulsa.pulsa = input('Masukan Pulsa : ')
                    pulsa.harga = int(input('Masukan Harga : '))

                    self.pulsaService.save()

                    input('Berhasil edit data')

                elif code == 4:
                    id = input('ID Pulsa [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    pulsa = self.pulsaService.findByKode(id)

                    if pulsa == None:
                        print('Pulsa itu tidak ada')
                        input()
                    
                    self.pulsaService.delete(pulsa)

                    input('Berhasil hapus data')

                elif code == 0:
                    return True
        elif code == 4:
            clear = True
            while True:
                if clear:
                    self.clear()
                    self.header()
                self.text_dedent('''
                1. Daftar PaketData
                2. Detail PaketData
                3. Tambah PaketData
                4. Edit PaketData
                5. Hapus PaketData
                0. Kembali
                ''')

                clear = True

                code = self.request()
                if code == 1:
                    filter = input('Filter berdasarkan jenis [kosongkan jika ingin tampilkan semua] : ')

                    paketdatas: List[PaketData] = None

                    if filter == '':
                        paketdatas = self.paketDataService.findAll()
                    else:
                        paketdatas = self.paketDataService.findByJenis(filter)

                    df = pd.DataFrame([(x.kode_paket(), x.name, x.harga, x.jenis) for x in paketdatas], columns=('ID', 'PaketData', 'Harga', 'Jenis'))

                    df.set_index('ID')

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    clear = False
                elif code == 2:
                    id = input('ID PaketData [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    paketData = self.paketDataService.findByKode(id)
                    if paketData == None:
                        print('PaketData itu tidak ada')
                        input()

                    self.text_dedent(f'''
                    Nama  : {paketData.name}
                    Harga : {paketData.harga}
                    Jenis : {paketData.jenis}
                    Deskripsi : 
                    --> {paketData.deskripsi}
                    ''')
                    input()
                elif code == 3:
                    paketData = PaketData()
                    paketData.jenis     = input('Masukan Jenis     : ')
                    paketData.name      = input('Masukan Nama      : ')
                    paketData.harga     = int(input('Masukan Harga     : '))
                    paketData.deskripsi = input('Masukan Deskripsi : ')

                    self.paketDataService.create(paketData)

                    input('Berhasil tambah data')
                elif code == 4:
                    id = input('ID PaketData [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    paketData = self.paketDataService.findByKode(id)

                    if paketData == None:
                        print('PaketData itu tidak ada')
                        input()
                    
                    paketData.jenis     = input('Masukan Jenis     : ')
                    paketData.name      = input('Masukan Nama      : ')
                    paketData.harga     = int(input('Masukan Harga     : '))
                    paketData.deskripsi = input('Masukan Deskripsi : ')

                    self.paketDataService.save()

                    input('Berhasil edit data')

                elif code == 5:
                    id = input('ID PaketData [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    paketData = self.paketDataService.findByKode(id)

                    if paketData == None:
                        print('PaketData itu tidak ada')
                        input()
                    
                    self.paketDataService.delete(paketData)

                    input('Berhasil hapus data')

                elif code == 0:
                    return True
        elif code == 5:
            pembelian_pulsas = self.pembelianService.findAllPulsa()
            pembelian_paketdatas = self.pembelianService.findAllPaketData()

            rows = []
            for x in pembelian_pulsas:
                rows.append((x.nomor, x.pulsa.id, x.pulsa.harga, x.pulsa.jenis, 'Pulsa', x.user.name))
            for x in pembelian_paketdatas:
                rows.append((x.nomor, x.paket.id, x.paket.harga, x.paket.jenis, 'PaketData', x.user.name))

            df = pd.DataFrame(rows, columns=('Nomor', 'ID', 'Harga', 'Jenis', 'Pembelian', 'User'))

            print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))
        elif code == 9:
            self.user = None
            return True
        elif code == 0:
            os._exit(0)
        return False

    def menu_user(self) -> bool:
        self.text_dedent('''
        1. Buat Pembelian
        2. Isi Saldo
        3. Riwayat Pembelian
        9. Logout
        0. Keluar
        ''')
        code = self.request()

        if code == 1:
            clear = True
            while True:
                if clear:
                    self.clear()
                    self.header()
                self.text_dedent('''
                1. Pulsa
                2. Paket Data
                0. Kembali
                ''')

                clear = True

                code = self.request()
                if code == 1:
                    filter = input('Filter berdasarkan jenis [kosongkan jika ingin tampilkan semua] : ')

                    pulsas: List[Pulsa] = None

                    if filter == '':
                        pulsas = self.pulsaService.findAll()
                    else:
                        pulsas = self.pulsaService.findByJenis(filter)

                    df = pd.DataFrame([(x.kode_pulsa(), x.pulsa, x.harga, x.jenis) for x in pulsas], columns=('ID', 'Pulsa', 'Harga', 'Jenis'))

                    df.set_index('ID')

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    id = input('ID Pulsa [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    pembelian = PembelianPulsa()

                    pembelian.pulsa = self.pulsaService.findByKode(id)

                    if pembelian.pulsa == None:
                        print('Pulsa itu tidak ada')
                        input()

                    pembelian.nomor = input('Masukan Nomor Hp : ')
                    pembelian.user = self.user

                    self.pembelianService.create(pembelian)

                    self.user.saldo -= pembelian.pulsa.harga
                    self.userService.update(self.user)

                    input('Berhasil melakukan pembelian')
                elif code == 2:
                    filter = input('Filter berdasarkan jenis [kosongkan jika ingin tampilkan semua] : ')

                    paketdatas: List[PaketData] = None

                    if filter == '':
                        paketdatas = self.paketDataService.findAll()
                    else:
                        paketdatas = self.paketDataService.findByJenis(filter)

                    df = pd.DataFrame([(x.kode_paket(), x.name, x.harga, x.jenis) for x in paketdatas], columns=('ID', 'PaketData', 'Harga', 'Jenis'))

                    df.set_index('ID')

                    print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

                    id = input('ID PaketData [-1 untuk batal] : ')

                    if id == '-1':
                        continue

                    pembelian = PembelianPaketData()

                    pembelian.paket = self.paketDataService.findByKode(id)

                    if pembelian.paket == None:
                        print('PaketData itu tidak ada')
                        input()

                    pembelian.nomor = input('Masukan Nomor Hp : ')
                    pembelian.user = self.user

                    self.pembelianService.create(pembelian)

                    self.user.saldo -= pembelian.paket.harga
                    self.userService.update(self.user)

                    input('Berhasil melakukan pembelian')
                elif code == 0:
                    return True

        if code == 2:
            id = input('Masukan Code Voucher [-1 untuk batal] : ')

            if id == '-1':
                return True

            voucher = self.voucherService.findByCode(id)

            if voucher == None:
                print('Voucher itu tidak ada')
                input()

            if voucher.used_by != None:
                print('Voucher sudah digunakan')
            else:
                self.voucherService.transaction(voucher, self.user)

                print('Berhasil mengisi saldo')

        elif code == 3:
            pembelian_pulsas = self.pembelianService.findAllPulsa()
            pembelian_paketdatas = self.pembelianService.findAllPaketData()

            rows = []
            for x in pembelian_pulsas:
                if x.user.id == self.user.id:
                    rows.append((x.nomor, x.pulsa.id, x.pulsa.harga, x.pulsa.jenis, 'Pulsa'))
            for x in pembelian_paketdatas:
                if x.user.id == self.user.id:
                    rows.append((x.nomor, x.paket.id, x.paket.harga, x.paket.jenis, 'PaketData'))

            df = pd.DataFrame(rows, columns=('Nomor', 'ID', 'Harga', 'Jenis', 'Pembelian'))

            print(tabulate.tabulate(df, headers=df.columns, tablefmt="pretty", showindex=False))

        elif code == 9:
            self.user = None
            return True
        elif code == 0:
            os._exit(0)

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

            try:
                if self.user == None:
                    self.login()
                    continue

                if self.menu():
                    continue

                if self.request_lanjut():
                    break
            except (ValueError, KeyboardInterrupt, IndexError):
                input('Inputan tidak valid')

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