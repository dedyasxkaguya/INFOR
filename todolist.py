tugas = []
User=input("Masukkan nama anda:")
while True:
    print("\n==== MENU TO-DO LIST ====")
    print("1. Tambah tugas")
    print("2. Lihat semua tugas")
    print("3. Keluar")
    print("=========================")

    pilih = input("Pilih menu (1-3): ")

    if pilih == "1":
        nama = input("Masukkan nama tugas: ")
        tugas.append(nama)
        print("Tugas berhasil ditambahkan!")
    
    elif pilih == "2":
        if len(tugas) == 0:
            print("Belum ada tugas yang ditambahkan.")
        else:
            print("\n📋 Daftar tugas:")
            for i in tugas:
                print("-", i)

    elif pilih == "3":
        print(f"Program selesai. Semangat ngerjain tugasnya {User} !")
        break

    else:
        print("Pilihan tidak ada, silahkan coba lagi.")