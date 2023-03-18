import random                                                         # importing random module                                                                              

def guess(pc_guess):                         # defined a function which takes an integer as argument
    guesses = 1                                    # set a variable named guesses value to 1 as default
    while True:                                                                 # created a while loop          
        user_guess = input("\nGuess the number computer picked : ")             # asks this
        if user_guess.isdigit() and int(user_guess) == pc_guess:     # if both these are true       
            print(f"\nYes the correct number is {pc_guess} and you have guessed it in {guesses}th try.")
            break                                                       # then we break the while loop
        guesses += 1             # and increment the variable guesses with 1 for each time in the loop

def game():                                     # defined a function named game()
    level = input("\nBy default this game is easy and there is medium and hard difficulty option.\n\
                  \nWhich difficulty do you want to play the game ? : ")  # which asks game difficulty
    if level.lower() == "medium":                                        # if user needs medium mode         
        print("\nFor Medium level number to guess will be form 1 to 25")
        guess(random.choice(range(1,26)))                            # user have to guess from 1 to 25 
    elif level.lower() == "hard":                                           
        print("\nFor Hard level number to guess will be from 1 to 50")      # if user needs hard mode
        guess(random.choice(range(1,51)))                           # user have to guess from 1 to 50
    else:
        print("\nThe difficulty mode is easy, guess numbers from 1 to 10")  # by default game is in easy
        guess(random.choice(range(1,11)))                           # user have to guess from 1 to 10
    while True:                                 # after the every game round this will ask to play again
        ask = input("\nDo you want to play the game again ?(yes/no) : ").lower()
        if ask != "no":                                         # if user says anything other than 'no'
            game()                                              # game will start from the beginning 
        else:
            print("\nThank you for playing the game !!")        # or else
            quit()                                              # the program will quit()
                
if __name__ == "__main__":
    print("Welcome to our guessing game")
    game()
else:
    print("This imported module contains the guess number game")
    game()
