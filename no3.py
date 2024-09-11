## Buatlah list sederhana berisikan minimal data diri 20 orang random yang berisi [Nama, Umur, TB, BB]. Kemudian lakukan operasi if-else sederhana untuk memfilter data dari list orang-orang yang anda buat.

# List dalam format [Nama, Umur, Tinggi Badan , Berat badan]
data_orang = [
    ["Zizi",17, 170, 55],
    ["Rifalina", 19, 160, 38],
    ["Rahmatia (ijah)", 18, 160, 55], 
    ["Apenx", 16, 150, 43],
    ["Diva", 20, 172, 57],
    ["Qonita ", 22, 155, 43],
    ["Fauziah", 24, 150, 39],
    ["Bagas", 25, 169, 54],
    ["Fadil", 27, 185, 90],
    ["Andro", 28, 172, 75],
    ["Bintang", 30, 166, 54],
    ["Faris", 13, 170, 60],
    ["Siti", 11, 150, 37],
    ["Iva", 15, 153, 40],
    ["Arsya", 16, 154, 50],
    ["Nadilla", 21, 163, 56],
    ["Rayi", 20, 168, 50],
    ["Yudho", 14, 165, 57],
    ["Bimo", 25, 167, 55],
    ["Billy", 23, 175, 70],
    ["Citra", 22, 158, 43],
]

# Membuat list kosong
orang = []

# Input user 
umur = int(input("Masukkan umur :  "))
tinggi = int(input("Masukkan tinggi badan : "))

# Filter
if umur <= data_orang [0][1] and tinggi <= data_orang[0][2] :
    orang.append(data_orang[0][0])
else:
    pass
if umur <= data_orang [1][1] and tinggi <= data_orang[1][2] :
    orang.append(data_orang[1][0])
else:
    pass
if umur <= data_orang [2][1] and tinggi <= data_orang[2][2]:
    orang.append(data_orang[2][0])
else:
    pass
if umur <= data_orang [3][1] and tinggi <= data_orang[3][2] :
    orang.append(data_orang[3][0])
else:
    pass
if umur <= data_orang [4][1] and tinggi <= data_orang[4][2] :
    orang.append(data_orang[4][0])
else:
    pass
if umur <= data_orang [5][1] and tinggi <= data_orang[5][2] :
    orang.append(data_orang[5][0])
else:
    pass
if umur <= data_orang [6][1] and tinggi <= data_orang[6][2] :
    orang.append(data_orang[6][0])
else:
    pass
if umur <= data_orang [7][1] and tinggi <= data_orang[7][2] :
    orang.append(data_orang[7][0])
else:
    pass
if umur <= data_orang [8][1] and tinggi <= data_orang[8][2] :
    orang.append(data_orang[8][0])
else:
    pass
if umur <= data_orang [9][1] and tinggi <= data_orang[9][2] :
    orang.append(data_orang[9][0])
else:
    pass
if umur <= data_orang [10][1] and tinggi <= data_orang[10][2] :
    orang.append(data_orang[10][0])
else:
    pass
if umur <= data_orang [11][1] and tinggi <= data_orang[11][2]:
    orang.append(data_orang[11][0])
else:
    pass
if umur <= data_orang [12][1] and tinggi <= data_orang[12][2] :
    orang.append(data_orang[12][0])
else:
    pass
if umur <= data_orang [13][1] and tinggi <= data_orang[13][2] :
    orang.append(data_orang[13][0])
else:
    pass
if umur <= data_orang [14][1] and tinggi <= data_orang[14][2]:
    orang.append(data_orang[14][0])
else:
    pass
if umur <= data_orang [15][1] and tinggi <= data_orang[15][2] :
    orang.append(data_orang[15][0])
else:
    pass
if umur <= data_orang [16][1] and tinggi <= data_orang[16][2] :
    orang.append(data_orang[16][0])
else:
    pass
if umur <= data_orang [17][1] and tinggi <= data_orang[17][2] :
    orang.append(data_orang[17][0])
else:
    pass
if umur <= data_orang [18][1] and tinggi <= data_orang[18][2] :
    orang.append(data_orang[18][0])
else:
    pass
if umur <= data_orang [19][1] and tinggi <= data_orang[19][2] :
    orang.append(data_orang[19][0])
else:
    pass

# Menampilkan data
print(f"Maka data nama yang memenuhi kriteria : {orang}")
