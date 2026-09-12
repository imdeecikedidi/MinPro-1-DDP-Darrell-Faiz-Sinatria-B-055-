film_data = [
    ("The Batman", "Action", 40000),
    ("Spirited Away", "Animation", 40000),
    ("Jujutsu Kaisen", "Fantasy", 40000)
]

while True:
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Ubah")
    print("4. Hapus")
    print("5. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        nama = input("Nama: ")
        kategori = input("Kategori: ")
        harga = int(input("Harga: "))
        film_data.append((nama, kategori, harga))

    elif pilih == "2":
        for i, film in enumerate(film_data, 1):
            print(i, film)

        input("Tekan Enter...")

    elif pilih == "3":
        nomor = int(input("Nomor: ")) - 1
        nama = input("Nama baru: ")
        kategori = input("Kategori baru: ")
        harga = int(input("Harga baru: "))
        film_data[nomor] = (nama, kategori, harga)

    elif pilih == "4":
        nomor = int(input("Nomor: ")) - 1
        del film_data[nomor]

    elif pilih == "5":
        print("Silahkan Dipilih selamat menonton")
        break