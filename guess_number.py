"""
    Program : Guess the number 
    Description : This is a basic python program to aims to make usage of syntax easier. When the 
                program begins , the user is expected to follow the program instructions . 
                This code contains no function or object. 
    Developer : Adeleke Bright 
    Last modified : 28-03-2020 
    Company       : ACE AFRICA (www.aceafrica.net)
""" 
from random import randint 
guesses = 0 
correct_guess = 0 

print("Welcome to Guess") 
game_card = [1 , 2 , 3 , 4 , 5 , 6]
start = int(input("To start press 1 : ")) 
if(start == 1) : 
    while ( guesses < 5) : 
        computer_guess = game_card[randint(1 , len(game_card) - 1)]
        guess_number = int(input("Guess a number between 1 and 6 to beat the computer : ")) 
        guesses += 1 
        if (computer_guess == guess_number) :
            print("Congratulations !!! You made a correct guess of {}".format(guess_number)) 
            correct_guess += 1 
        else : 
            print("You made a wrong guess , please try again. The number is {}".format(computer_guess)) 
        play_again = input("press q to quit or any other key to continue:  ") 
        end_code = ["q" , "Q"]
        if (play_again in end_code) :
          break
        else :
            continue 
    rank_player = (correct_guess/guesses)*100 
    terminal_msg = "You got {:>3.2f} % after {} trials" 
    print(terminal_msg.format(rank_player , guesses)) 
else :
    print("Thanks for quitting . We hope you play another") 
    