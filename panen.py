def hitung_total_panen(hasil_panen):
    return sum(hasil_panen)


def hitung_diskon(total, persen_diskon=10):
    diskon = total * persen_diskon / 100
    return total - diskon


hasil = [100, 150, 200, 125]

total = hitung_total_panen(hasil)
total_setelah_diskon = hitung_diskon(total)

print("Hasil panen:", hasil)
print("Total hasil panen:", total, "kg")
print("Total setelah diskon:", total_setelah_diskon, "kg")
