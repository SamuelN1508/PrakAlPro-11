Data = ('Samuel Natanael', '71231050', 'Kotabaru, DI Yogyakarta')
print(f'NIM = {Data[1]}')
print(f'NAMA = {Data[0]}')
print(f'ALAMAT = {Data[2]}')

nim = tuple(Data[1])
nama = Data[0].split()
nama_depan = nama[0]
nama_terbalik = nama[::-1]
print(nim)
print(tuple(nama_depan))
print(tuple(nama_terbalik))