buah = ["Jagung","Kiwi","Apel",
        "Alpukat","Anggur","Mangga",
        "Jeruk","Pepaya","Nanas",
        "Rambutan"]

print("Data awal\t :\n",buah)

buah.remove(buah[0])
print("Data buah setelah penghapusan indeks ke - 0\t :\n",buah)

if "Jagung" not in buah or "Jeruk" not in buah:
    buah.append("Jagung")
    print("Data buah setelah penambahan\t :\n",buah)
else:
    print("sudah ada jagung atau jeruknya")


buah_sort_by_abjad = []
while buah:
    data_pertama = buah[0]
    for i in buah:
        if i < data_pertama:
            data_pertama = i
    buah_sort_by_abjad.append(data_pertama)
    buah.remove(data_pertama)
print("Data disort berdasarkan abjad\t : \n",buah_sort_by_abjad)
buah_sort_by_length = []
while buah_sort_by_abjad:
    data_pertama = buah_sort_by_abjad[0]
    for i in buah_sort_by_abjad:
        if len(i) < len(data_pertama):
            data_pertama = i
    buah_sort_by_length.append(data_pertama)
    buah_sort_by_abjad.remove(data_pertama)

print("Data disort berdasarkan panjang string\t : \n",buah_sort_by_length)
