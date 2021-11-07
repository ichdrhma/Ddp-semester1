print('SLTP GAJI PT. XYZ')
print('----------------------------')


nama = (0, 'Ahmad', 'Alex')
agama = (0, 'Islam', 'Kristen Protestan')
anak = (0, 2, 5)
gaji = (0, 4000000, 6000000)

angka = 2
for no in range(angka):
    no += 1


    tunj_jabatan = gaji[no] + gaji[no] * 20 / 100
    tunj_keluarga = ''
    if(anak[no] <= 2):
        tunj_keluarga = gaji[no] * 10 / 100
    elif(anak[no] >= 2):
        tunj_keluarga = gaji[no] * 20 / 100
    else:
        tunj_keluarga = 0
    gaji_kotor = gaji[no] + tunj_jabatan + tunj_keluarga

    zakat = (0, 0.025)[agama[no] == 'Islam' and gaji_kotor >= 6000000] * gaji_kotor
    total = gaji_kotor - zakat





    print("Nama \t\t\t: ", nama[no])
    print('Agama \t\t\t: ', agama[no])
    print('Jumlah anak \t\t: ', anak[no])
    print('Gaji pokok \t\t: Rp. ', gaji[no] )
    print('Tunjangan Jabatan \t: Rp. ', tunj_jabatan)
    print('Tunjangan Keluarga \t: Rp. ', tunj_keluarga)
    print('Gaji Kotor \t\t: Rp. ', gaji_kotor)
    print('Zakat Profesi \t\t: Rp. ', zakat)
    print('Take Home Pay \t\t: Rp. ', total, '\n')

    

    print('SLTP GAJI PT. XYZ')
    print('----------------------------')


