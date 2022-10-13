import random

def board(lives):
    if lives == 6:
        print("+-----+")
        print("|      ")
        print("|      ")
        print("|      ")
        print("|______")
    elif lives == 5:
        print("+-----+")
        print("|     O")
        print("|      ")
        print("|      ")
        print("|______")
    elif lives == 4:
        print("+-----+")
        print("|     O")
        print("|     |")
        print("|      ")
        print("|______")
    elif lives == 3:
        print("+-----+")
        print("|     O")
        print("|    /|")
        print("|      ")
        print("|______")
    elif lives == 2:
        print("+-----+")
        print("|     O")
        print("|    /|\\")
        print("|      ")
        print("|______")
    elif lives == 1:
        print("+-----+")
        print("|     O")
        print("|    /|\\")
        print("|    / ")
        print("|______")

def again():
    again = input("Do you want to play again? 'y' or 'n': ")
    if again == 'y':
        hangman()
    else:
        exit()

def hangman():
    words = ["hello","computer","latitude","notebook","book","board","pencil","marker","cube","cars",
            "wonder","water","happy","survive","resurgence","supply","rebirth","island","loadout","countdown"]
    word = random.choice(words)
    word_letters = set(word)
    used_letters = set()
    length = len(word)
    lives = 6
    while len(word_letters) > 0 or lives > 0:
        print('-'*length)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        board(lives)
        print("Current word: ", " ".join(word_list))
        user = input("Guess a Letter: ")
        if user in word_letters:
            word_letters.remove(user)
            used_letters.add(user)
        elif user in used_letters:
            print("You've already guessed this letter!!")
        else:
            lives = lives - 1
            print("Incorrectly Guessed")

        if len(word_letters) == 0:
            print("You correctly guessed " +word+ '!!')
            again()
        elif lives == 0:
            print("You Died!")
            print("+-----+")
            print("|     o")
            print("|    /|\\")
            print("|    / \\")
            print("|______")
            print("The correct word was " + word)
            again()

hangman()