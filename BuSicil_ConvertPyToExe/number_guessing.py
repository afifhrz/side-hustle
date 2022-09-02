# converting to exe
# template

# workingspace
# input
number_user = int(input("Silahkan masukkan angka yang akan ditebak?"))

# proses game
import random
random_number = int(random.randint(1, 10))
print(random_number)

while True:
    if number_user == random_number:
        print("tebakan benar")
        break
    else:
        print("tebakan salah")
        if number_user > random_number:
            print("It's Higher!")
        else:
            print("It's Lower!")
        number_user = int(input("Silahkan masukkan angka yang akan ditebak?"))