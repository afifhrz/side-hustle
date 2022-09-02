import requests
import random

from sklearn.utils import check_array

link = "https://www.mit.edu/~ecprice/wordlist.10000"
r = requests.get(link)
bank_word = r.text.split('\n')

play = input("Enter to continue!")
print("Welcome to game typing!\nRe-Type the word!")
while play.lower != "stop the game":
    check_word = bank_word[random.randint(0,len(bank_word))]
    print(check_word)
    while True:
        play = input("Your answer here---> ")
        if play == check_word:
            print("Great!")
            break
        elif play.lower != "stop the game":
            exit()
        else:
            print("Incorrect!")
            print("Re-Type the word:\t",check_word)
            print('if you want quit the game please type "stop the game"')