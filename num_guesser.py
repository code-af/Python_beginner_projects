import random

def guess(pc_guess):
    guesses = 1
    while True:
        user_guess = input("\nGuess the number computer picked : ")
        if user_guess.isdigit() and int(user_guess) == pc_guess:
            print(f"\nYes the correct number is {pc_guess} and you have guessed it in {guesses}th try.")
            break
        guesses += 1

def game():
    level = input("\nBy default this game is easy and there is medium and hard difficulty option.\n\
                  \nWhich difficulty do you want to play the game ? : ")
    if level.lower() == "medium":
        print("\nFor Medium level number to guess will be form 1 to 25")
        guess(random.choice(range(1,26)))
    elif level.lower() == "hard":
        print("\nFor Hard level number to guess will be from 1 to 50")
        guess(random.choice(range(1,51)))
    else:
        print("\nThe difficulty mode is easy, guess numbers from 1 to 10")
        guess(random.choice(range(1,11)))
    while True:
        ask = input("\nDo you want to play the game again ?(yes/no) : ").lower()
        if ask != "no":
            game()
        else:
            print("\nThank you for playing the game !!")
            quit()
                
if __name__ == "__main__":
    print("Welcome to our guessing game")
    game()
else:
    print("This imported module contains the guess number game")
    game()