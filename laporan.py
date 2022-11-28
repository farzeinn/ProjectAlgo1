import pandas as pd

df = pd.read_csv('bijikopi.csv')
df = df.astype({'bulan':str, 'tahun':str})

products = df['produk'].unique()
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