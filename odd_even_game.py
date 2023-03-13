# odd or even ask ->player_choice odd/even, if player_choice is true = choice[bat/bowl]
# if player choose bat, while loop strike=,computer_choice random(range(7))
# while the computer choice != striker player_score.append(striker choice)
import functools  # importing functools because we need reduce method
import random  # we also need choice method for pc

user_score = []  # created an empty list for storing game scores of user
pc_score = []  # created an empty list for storing game scores of computer
runs_choice = [0, 1, 2, 3, 4, 5, 6]  # created a list of numbers from 1 to 6

def user_innings():  # created a function for user's innings and pc's chase innings inside it
    while True:
        chooser = 0
        chooser = int(input("Enter the batting numbers : "))
        bowler = random.choice(runs_choice)  # the computer selects random number from 1 to 6
        print("The bowler chose >>", bowler)
        if chooser not in runs_choice:  # if user entered any invalid number the run will be 0 by default
            chooser = 0
        if chooser == bowler:  # if the batsman entered number is equivalent to the bowler entered number then it's out
            print("The batsman is out !!\n","_" * 75)
            total_user_score = functools.reduce(lambda x, y: x + y, user_score)  # using lambda function to add up score
            break
        user_score.append(chooser)  # appending the score list with all the batsman entered runs excluding outs
    print(f"The total score for chasing is {total_user_score}\n", "_" * 75)

    def pc_chase_innings():  # created another function inside the function for user_innings for pc's chase innings
        print("computer is chasing now\n", "_" * 75)
        while True:
            chooser = 0
            bowler = int(input("Enter the bowling numbers : "))  # here we are bowlers, so we have to enter the numbers
            chooser = random.choice(runs_choice)
            print("The batter chose >>", chooser)
            if chooser == bowler:
                print("The batsman is out !!\n", "_" * 75)
                total_pc_score = functools.reduce(lambda x, y: x + y, pc_score)
                break
            pc_score.append(chooser)
        print(f"The total score by the chaser is {total_pc_score}\n", "_" * 75)
        if total_pc_score < total_user_score:  # using if structures for comparing user's and pc's scores
            win_margin = total_user_score - total_pc_score  # user wins if user's score is highest
            print(f"the user has won with the score difference of {win_margin} runs.\n", "_" * 75)
        elif total_pc_score > total_user_score:  # elif pc's score is the highest then pc wins the game
            win_margin = total_pc_score - total_user_score  # and the difference of runs are stored in this variable
            print(f"the pc has won with the score difference of {win_margin} runs.\n", "_" * 75)
        else:  # if they both have equal scores
            print("The game has concluded in a draw")  # then the game ended in a draw
    pc_chase_innings()  # after creating the function inside the outer function we called it within the outer function

def pc_innings():  # created a function for pc's innings and user's chase innings inside it
    while True:
        chooser = 0
        bowler = int(input("Enter the bowling numbers : "))
        chooser = random.choice(runs_choice)
        print("The batter chose >> ",chooser)
        if chooser == bowler:
            print("The batsman is out !!\n", "_" * 75)
            total_pc_score = functools.reduce(lambda x, y: x + y, pc_score)
            break
        pc_score.append(chooser)
    print(f"The total score for chasing is {total_pc_score}\n", "_" * 75)

    def user_chase_innings():
        print("user is chasing now\n", "_" * 75)
        while True:
            chooser = 0
            chooser = int(input("Enter the batting numbers : "))
            bowler = random.choice(runs_choice)
            print("The bowler chose >> ", bowler)
            if chooser not in runs_choice:
                chooser = 0
            if chooser == bowler:
                print("The batsman is out !!\n", "_" * 75)
                total_user_score = functools.reduce(lambda x, y: x + y, user_score)
                break
            user_score.append(chooser)
        print(f"The total score by the chaser is {total_user_score}\n", "_" * 75)
        if total_pc_score < total_user_score:
            win_margin = total_user_score - total_pc_score
            print(f"the user has won with the score difference of {win_margin} runs.\n", "_" * 75)
        elif total_pc_score > total_user_score:
            win_margin = total_pc_score - total_user_score
            print(f"the pc has won with the score difference of {win_margin} runs.\n", "_" * 75)
        else:
            print("The game has concluded in a draw")
    user_chase_innings()

def play():  # creating another function as play which is the main function to call the above functions in it.
    try:  # using try-except block
        odd_even_choice = input("Odd or Even : ").lower()  # asking user for odd or even
        odd_even_user = int(input("Enter any number from 1 to 6 : "))  # once they say odd, or even we ask them for nums
        print("The computer has chosen >> ",odd_even_pc := random.choice(runs_choice))  # used walrus for instance
        if (odd_even_pc + odd_even_user) % 2 == 0 and odd_even_choice == "even" or\
                (odd_even_pc + odd_even_user) % 2 != 0 and\
                odd_even_choice == "odd":  # if condition to check when user winning his toss
            bat_bowl = input("You won the toss, do you want to bat or bowl ? : ")  # if user wins we print this
            if bat_bowl == "bat":  # if user says bat
                print("The user is batting and the computer is bowling\n", "_" * 75)
                user_innings()  # we call the user_innings function for user's batting
            else:  # if user chose bowl
                print("The user chosen bowling and the computer is batting\n", "_" * 75)
                pc_innings()  # we call the pc_innings function to start the computers batting

        else:  # if the computer wins the toss
            print("The computer has won the toss and chose to", bat_bowl := random.choice(["bowl", "bat"]))  # bat/bowl
            if bat_bowl == "bat":  # if computer randomly picks bat option
                print("The computer is batting and the user is bowling\n", "_" * 75)
                pc_innings()  # we will start the computer's batting innings function
            else:  # if computer chose bowl
                print("The computer chosen bowling and the user is batting\n", "_" * 75)
                user_innings()  # we then call the function for user's batting
    except TypeError or ValueError or SyntaxError or Exception:  # using except block for error checking
        print("I think the game has already ended before it even got started play again\n", "_" * 75)  # which says this
        play()  # if there is any error we called the function inside the function to restart the game
if __name__ == "__main__":  # using if __name__ == __main__ for checking the module's originality
    print("This is a game gimmick of  the sport cricket ")
    play()  # calling the play function to start the game
else:  # else when the module is imported we print the message below
    print("This module is being imported , this module includes a game")
    play()  # calling the play function to start the game