col = int(input())
row = int(input())

angka = 1

for baris in range(row):
    # do something
    hasilbaris = ""
    for kolom in range(col):
        # do something
        hasilbaris = hasilbaris + str(angka) + " "
        angka = angka + 1
    print(hasilbaris)