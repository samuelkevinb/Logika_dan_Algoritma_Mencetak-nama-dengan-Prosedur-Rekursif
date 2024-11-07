def cetak_nama(nama, count=1):
    if count > 100:  # Berhenti jika sudah mencetak 100 kali
        return
    print(nama)
    cetak_nama(nama, count + 1)  # Memanggil fungsi secara rekursif dengan menambah hitungan

# Memanggil fungsi dengan nama Anda
cetak_nama("Samuel Kevin")
