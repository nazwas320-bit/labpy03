saldo = 1000000  # saldo awal

while True:
    print("\nSaldo saat ini: Rp", saldo)
    print("1. Tarik Uang")
    print("2. Keluar")

    menu = int(input("Pilih menu (1/2): "))

    if menu == 1:
        tarik = int(input("Masukkan jumlah penarikan: "))
        if tarik <= saldo:
            saldo -= tarik
            print("Penarikan berhasil!")
        else:
            print("Saldo tidak cukup!")

    elif menu == 2:
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

    # jika saldo sudah habis
    if saldo == 0:
        print("Saldo Anda telah habis. Terima kasih telah menggunakan ATM!")
        break
