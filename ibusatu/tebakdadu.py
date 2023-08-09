def tebakCangkir(N, T, P, posisi):
    # Write your code here
    dadu = [0]*N
    dadu[P-1] = 1
    for i in range(T):
        origin, destination = posisi[i]
        item = dadu.pop(origin-1)
        dadu.insert(destination-1, item)
    return dadu.index(1)+1