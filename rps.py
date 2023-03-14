import random                                                                            # we need random choices
game_choice = ["rock","paper", "scissors"]                                                          # game options
total_rounds = 10                                                                       # total rounds of gameplay

def gameplay(user_score,pc_score):                                             # created a function named gameplay
    while (user_score+pc_score) <= total_rounds:                                # while loop with a limit to run
        user = input("Rock, Paper, Scissors : ").lower()
        while user in game_choice:              # only print the computers choice when user enters a valid option
            print("_"*75,"\nThe computer chooses >>", pc := random.choice(game_choice),"\n","_"*75)
            break
        if user == "rock" and pc == "scissors" or user == "scissors" and\
            pc == "paper" or user == "paper" and pc == "rock":          # checking if the user wins the round
            print("1 point for the User \n","_"*75)
            user_score+= 1                                              # the parameter of user score will append           
        if pc == "rock" and user == "scissors" or pc == "scissors" and\
            user == "paper" or pc == "paper" and user == "rock":                     # if pc wins the round
            print("1 point for the Computer\n","_"*75)
            pc_score+= 1                                                 # the parameter of pc score will append           
        if user == pc:                                                                     # when both are equal
            print("Game Tied, 0 points for both\n","_"*75)                                        # round tied   
        if user not in game_choice or user_score > (total_rounds/2) or pc_score > (total_rounds/2):
            if user_score > pc_score:             # user can end the game or any of them can win based on points
                print(f"User has won the game leading with {user_score} points, the computer has {pc_score} points.\n","_"*75)
            elif user_score < pc_score:                           # checking if user score or pc score is higher
                print(f"The computer has won the game with points of {pc_score}, the user has only {user_score}\n","_"*75)
            else:                                         # game ends in a tie when both of them have same points
                print(f"The game ended in a draw with both user and pc sharing {user_score}-{pc_score} each\n","_"*75)
            print(end=" "*37 + "GAME OVER\n" + "_"*75)             # then we print these messages along with it 
            break
    def play_again():                      # defining another function for restarting the game again with choices
        ask = input("\nDo you want to play the game again ?(yes/no) : ").lower()
        if ask != "no":                                     # if user puts anything other than no, game restarts
            gameplay(user_score=0,pc_score=0)              # we call the gameplay function with default arguments
        else:
            print(end=" "*37 + "GAME ENDED\n" + "_"*75)
            quit()                                          # if the user don't want to play we quit the program
    play_again()                                       # we called the playagain() function inside the gameplay()
                                                            #  so when the gameplay() ends this one starts
if __name__ == "__main__":                                          
    print("This is running from the original module.\n","_"*75)
    gameplay(0,0)
else:
    print("This module is an imported module.\n","_"*75)
    gameplay(0,0)