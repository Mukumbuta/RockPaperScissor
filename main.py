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
    menu_choice = input("Enter:\n 1. To Play\n 2. To Exit\n")
    if menu_choice == str(1):
        def rockPaperScissor():
            global options
            options = [ 'r', 'p', 's' ]
            CPU = random.choice(options)
            return CPU
        CPU = rockPaperScissor()

        value = True
        while value == True:
            Player = input("<<<<<>>>>>> Enter Your Choice <<<<<>>>>>>\n => R for Rock\n => P for Paper or\n => S for Scissor\n").lower()
            print()

            if Player not in options:
                print("Please check your spelling and Try Again!\n")
                value 

            elif (Player == 'r' and CPU == 'r') or (Player == 'p' and CPU == 'p') or (Player == 's' and CPU == 's'):
                print(f'Player ({Player.title()}) : CPU ({CPU.title()})')
                print("It's a Tie. Try Again!\n")
                value 

            elif (Player == 'r' and CPU == 'p') or (Player == 'p' and CPU == 's') or (Player == 's' and CPU == 'r'):
                print(f'Player ({Player.title()}) : CPU ({CPU.title()})')
                print("CPU\n")
                value = False
 
            elif (Player == 'p' and CPU == 'r') or (Player == 's' and CPU == 'p') or (Player == 'r' and CPU == 's'):
                print(f'Player ({Player.title()}) : CPU ({CPU.title()})')
                print("Player\n")
                value = False
           
    elif menu_choice == str(2):
        print("Bye!")
        sys.exit()

    else:
        print("Invalid value! Press 1 or 2\n")


    