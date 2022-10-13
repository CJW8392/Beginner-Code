import random

def game():
    user = input("Select 'r' for rock, 'p' for paper, or 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print("You played " +user)
    print("Computer played " +computer)
    
    if user == computer:
        print("It's a draw!")
    elif user == 'r' and computer == 's' or user == 'p' and computer == 'r' or user == 's' and computer == 'p':
        print("User wins!")
    else:
        print("Computer wins!")

    again = input("Do you wish to play again? 'y' or 'n': ")
    if again == 'y':
        game()
    else:
        exit()

game()