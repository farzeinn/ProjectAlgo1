from laporan import show_laporan, add_data, show_data, show_latest_data, update_data, del_data
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
        print('login berhasil!')
        login = True
        break
    else:
        print('username atau password salah!')
    if i == 2:
        print('Anda gagal login ke sistem, silahkan jalankan ulang program')
while login == True:
    print('\n','='*10, 'SELAMAT DATANG DI SISTEM PENCATATAN BIJI KOPI', '='*10)
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
        
    elif inputan == '2':
        input_data = True
        print('Anda akan menambahkan data baru')
        print('''\nlist produk :
        (0) : arabika toraja
        (1) : arabika blue ijen
        (2) : arabika gayo
        (3) : arabika kintamani
        (4) : robusta bogor
        (5) : robusta gayo
        (6) : arabika papua wamena
        (7) : robusta dampit''')
        print('\n~ Masukan berupa angka dari kode produk')
        while input_data == True:
            try:
              produk = input('masukkan kode produk : ')
              harga = int(input('masukkan harga : '))
              bulan = input('masukkan bulan : ')
              tahun = input('masukkan tahun : ')
              kode_produk = ['0','1','2','3','4','5','6','7']
              if produk in kode_produk:
                print(f'''data baru :
    bulan = {bulan} 
    tahun = {tahun}
    kode produk = {produk}
    harga = {harga}''')
                print('pastikan kembali data baru sudah benar!')
                input_data = input('apakah data yang akan anda tambahkan sudah benar? (y/n) : ')
                if input_data == 'y' or input_data == 'Y':
                  add_data(bulan, tahun, produk, harga)
                  print('Data berhasil ditambahkan!')
                  print('Anda akan ditujukan keluar dari program untuk merefresh data penjualan terkini')
                  input_data = False
                  login = False
                else:
                  input_data = True
              else:
                print('kode produk tidak sesuai!')
                input_data = False
            except:
                print('harga harus berupa angka!')

    elif inputan == '3':
        print('''Anda akan mengelola data
        1. Lihat data
        2. Perbarui data
        3. Hapus data''')
        inputan_kelola = input('masukkan pilihan : ')
        if inputan_kelola == '1':
            print('1. lihat data terbaru \n2. lihat data berdasarkan bulan dan tahun')
            inputan_kelola = input('masukkan pilihan : ')
            if inputan_kelola == '1':
                print('Anda akan melihat data penjualan terbaru')
                show_latest_data()
            elif inputan_kelola == '2':
                print('Anda akan melihat data penjualan berdasar bulan dan tahun')
                bulan = input('masukkan bulan : ')
                tahun = input('masukkan tahun : ')
                show_data(bulan, tahun)
        elif inputan_kelola == '2':
            index = True
            print('Anda akan memperbarui data')
            while index == True:
                try:
                    idx = int(input('masukkan index dari data : '))
                    update_data(idx)
                    index = False
                    login = False
                except:
                    print('index harus berupa angka')
        elif inputan_kelola == '3':
            index = True
            print('Anda akan menghapus data')
            print("ketik '-' untuk kembali")
            while index == True:
                try:
                    idx = str(input('masukkan index dari data : '))
                    if idx == '-':
                        index = False
                    else:
                        del_data(int(idx))
                        index = False
                        login = False
                except:
                    print('index harus berupa angka')
                
    elif inputan == '4':
        login = False
    else:
        print('Inputan tidak sesuai!')