from laporan import show_laporan
#pip install pwinput
from pwinput import pwinput

username = 'admin'
passw = 'admin123'
login = False
print('='*10, 'LOGIN SISTEM PENCATATAN BIJI KOPI', '='*10)
for i in range(3):
    login_username = str(input('masukkan username : '))
    login_passw = pwinput('masukkan password : ')
    #login_passw = str(input('masukkan password : '))
    if (login_username == username) and (login_passw == passw):
        print('login berhasil!\n')
        login = True
        break
    else:
        print('username atau password salah!')
    if i == 2:
        print('Anda gagal login ke sistem, silahkan jalankan ulang program')
while login == True:
    print('='*10, 'SELAMAT DATANG DI SISTEM PENCATATAN BIJI KOPI', '='*10)
    print('''
          1. Laporan Penjualan
          2. Tambah Data
          3. Kelola Data
          4. Keluar
          ''')
    inputan = str(input('masukkan pilihan : '))
    if inputan == '1':
        print('Anda akan melihat laporan penjualan')
        bulan = input('masukkan bulan : ')
        tahun = input('masukkan tahun : ')
        show_laporan(bulan, tahun)
        
    elif inputan == '4':
        login = False