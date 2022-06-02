import random
import sys



print(
    """
        <<<<>>>>>> ROCK PAPER SCISSOR GAME <<<<<<>>>>>
    <<<<<<<<<<<<<<<<<<<<<< Welcome >>>>>>>>>>>>>>>>>>>>
        <<<<<<<<>>>>>>>>> Game Menu <<<<<<<>>>>>>>>>
                        1. Play
                        2. Exit\n
    """
)

print(
    """
        ############## How To Play ##############
            Rock  vs Paper -> Paper wins
            Rock  vs Scissor -> Rock wins
            Paper vs Scissor -> Scissor wins.
            A tie is declared when the Computer’s choice and the User’s choice are the same.
            The User will get to choose another option. 
            The game will be played until the loser or the winner is declared. 
    """
)


while True:
    play_exit = input("Enter:\n 1. To Play\n 2. To Exit\n")
    if play_exit == str(1):
        def rockPaperScissor():
            global options
            options = [ 'r', 'p', 's' ]
            computer_choice = random.choice(options)
            return computer_choice
        computer_choice = rockPaperScissor()

        value = True
        while value == True:
            player_choice = input("<<<<<>>>>>> Enter Your Choice <<<<<>>>>>>\n => R for Rock\n => P for Paper or\n => S for Scissor\n").lower()
            print()

            if player_choice not in options:
                print("Please check your spelling and Try Again!\n")
                value 

            elif (player_choice == 'r' and computer_choice == 'r') or (player_choice == 'p' and computer_choice == 'p') or (player_choice == 's' and computer_choice == 's'):
                print("Your choice: ", player_choice.title())
                print("Computer's choice: ", computer_choice.title())
                print("It's a Tie. Try Again!\n")
                value 

            elif (player_choice == 'r' and computer_choice == 'p') or (player_choice == 'p' and computer_choice == 's') or (player_choice == 's' and computer_choice == 'r'):
                print("Your choice: ", player_choice.title())

                print("Computer's choice: ", computer_choice.title())
                print("Sorry. You lost!\n")
                value = False
 
            elif (player_choice == 'p' and computer_choice == 'r') or (player_choice == 's' and computer_choice == 'p') or (player_choice == 'r' and computer_choice == 's'):
                print("Your choice: ", player_choice.title())
                print("Computer's choice: ",computer_choice.title())
                print("Congratulations! You won!\n")
                value = False
           
    elif play_exit == str(2):
        print("Bye!")
        sys.exit()

    else:
        print("Invalid value! Press 1 or 2\n")


    