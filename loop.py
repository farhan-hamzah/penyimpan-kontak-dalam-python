kontak = { 
    'Nama ': ["Farhan", "Ayu"], 
    'NIM ': ["103012400018", "0000"], 
    'Email ': ["farhanhamzah@gmail.com", "Ayubla"]
    }
i = 0
while True:
    print("\n Menu Kontak")
    print("1. Melihat Kontak")
    print("2. Menambah Kontak")
    print("3. Menghapus Kontak")
    print("4. Keluar dari Kontak")

    pilihan = int(input("Masukan Pilihan Menu :", ))

    if pilihan == 1:
        print("\nKontak:")
        for i in range(len(kontak['Nama '])):
            print(f"Nama: {kontak['Nama '][i]}")
            print(f"NIM: {kontak['NIM '][i]}")
            print(f"Email: {kontak['Email '][i]}")
            i+=1

    elif pilihan == 2:
        print("Masukan Nama :"),kontak['Nama '].append(input())
        print("Masukan NIM :"),kontak['NIM ' ].append(input())
        print("Masukan Email :"),kontak['Email ' ].append(input())
        pass

    elif pilihan == 3:
        print("Masukan Data Yang Ingin Dihapus")
        hapus = int(input())
        kontak['Nama '].pop(hapus)
        kontak['NIM '].pop(hapus)
        kontak['Email '].pop(hapus)
        print("Kontak Berhasil Dihapus")
        
    elif pilihan == 4:
        print("Terima Kasih")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        pass