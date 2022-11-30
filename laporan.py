import pandas as pd

df = pd.read_csv('bijikopi.csv')
df = df.astype({'bulan':str, 'tahun':str})

products = df['produk'].unique()
prod_dict = {
'0':'arabika toraja','1':'arabika blue ijen','2':'arabika gayo','3':'arabika kintamani',
'4':'robusta bogor','5':'robusta gayo','6':'arabika papua wamena','7':'robusta dampit'
}
def show_laporan(bulan, tahun):
  if df[(df['bulan'] == bulan) & (df['tahun'] == tahun)].empty:
    print(f'Laporan Penjualan Bulan {bulan} Tahun {tahun} Tidak Ditemukan')
  else:
    print(f'--- Laporan Penjualan Bulan {bulan} Tahun {tahun} ---')
    print('total barang terjual \t\t\t\t\t:', df[(df['bulan'] == bulan) & (df['tahun'] == tahun)]['harga_produk'].count())
    print('total pendapatan kotor \t\t\t\t\t:', df[(df['bulan'] == bulan) & (df['tahun'] == tahun)]['harga_produk'].sum())
    for i in products:
      print(f'total penjualan produk {i} \t\t:', df[(df['bulan'] == bulan) & (df['tahun'] == tahun) & (df['produk'] == i)]['harga_produk'].count())
      print(f'total pendapatan produk {i} \t\t:', df[(df['bulan'] == bulan) & (df['tahun'] == tahun) & (df['produk'] == i)]['harga_produk'].sum())

def add_data(bulan, tahun, produk, harga):
    new_data = {'bulan':bulan, 'tahun':tahun, 'produk':prod_dict[produk], 'harga_produk':harga}
    global df
    df = df.append(new_data, ignore_index = True)
    df.to_csv('bijikopi.csv', index=False)

def show_data(bulan, tahun):
  if df[(df['bulan'] == bulan) & (df['tahun'] == tahun)].empty:
    print(f'Laporan Penjualan Bulan {bulan} Tahun {tahun} Tidak Ditemukan')
  else:
    print(df[(df['bulan'] == bulan) & (df['tahun'] == tahun)])

def show_latest_data():
  print(df.tail(20))

def update_data(idx):
  try:
    if df.loc[idx].any():
      print(df.loc[idx])
      update_data = input('anda akan memperbarui data di atas? (y/n) : ')
      if update_data == 'y' or update_data == 'Y':
        input_data = True
        print('Anda akan memperbarui data di atas')
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
            kode_produk = '01234567'
            if produk in kode_produk:
              print(f'''data baru :
              bulan = {bulan} 
              tahun = {tahun}
              kode produk = {produk}
              harga = {harga}''')
              print('pastikan kembali data yang baru sudah benar!')
              input_data = input('apakah data yang akan anda tambahkan sudah benar? (y/n) : ')
              if input_data == 'y' or input_data == 'Y':
                df.loc[idx] = [bulan, tahun, prod_dict[produk], harga]
                df.to_csv('bijikopi.csv', index=False)
                input_data = False
              else:
                input_data = True
            else:
              print('kode produk tidak sesuai!')
              input_data = False
          except:
            print('Error! harga harus berupa angka')
      else:
          print('Anda akan ditujukan keluar dari program')
  except:
    print('data tidak ditemukan')
    
def del_data(idx):
  global df
  try:
    if df.loc[idx].any():
      print(df.loc[idx])
      delete_data = input('anda akan menghapus data di atas? (y/n) : ')
      if delete_data == 'y' or delete_data == 'Y':    
          df = df.drop(idx)
          print('Data berhasil dihapus!')
          print('Anda akan ditujukan keluar dari program untuk merefresh data penjualan terkini')
          df.to_csv('bijikopi.csv', index=False)
      else:
          print('Anda akan ditujukan keluar dari program')
    
  except:
    print('data tidak ditemukan')