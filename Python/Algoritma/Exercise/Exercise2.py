def penghitung_jumlah_gaji():
    nama = input('masukan nama : ')
    jam_kerja = int(input('jam kerja (jam): '))
    tarif_perjam = 30000 
    jumlah_gaji = tarif_perjam * jam_kerja
    print('nama         :',nama)
    print('jam kerja    :',str(jam_kerja),'jam')
    print('tarif_perjam :',tarif_perjam)
    print('jumlah gaji  :',jumlah_gaji)
penghitung_jumlah_gaji()
