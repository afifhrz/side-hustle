nilai_1 = int(input())
nilai_2 = int(input())
nilai_3 = int(input())
nilai_4 = int(input())
nilai_5 = int(input())

nilai_1 = nilai_1 * 1
nilai_2 *= 2
nilai_3 *= 5
nilai_4 *= 10
nilai_5 *= 20

total = nilai_1 + nilai_2 + nilai_3 + nilai_4 + nilai_5
total /= 100
total = "%.2f" % total

print("You have",total,"euro!")