def sort_median(ini_list):
    
    cek_list = ini_list.copy()
    hasil = []

    for angka in ini_list:
        # do_something
        minimum = min(cek_list)
        cek_list.remove(minimum)
        hasil.append(minimum)
    
    return hasil

print(sort_median([6,5,4]))