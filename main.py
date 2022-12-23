import random

comp_score = 0
user_score = 0


def get_user_choice():
    """Ask user whether they want rock, paper, or scissors"""

    while True:
        user_choice = input("\nRock, Paper, or Scissors? ").title()

        if user_choice == "Rock" or user_choice == "Paper" or user_choice == "Scissors":
            break

    return user_choice


def get_computer_choice():
    """Generate a random number and asign it a choice"""

    number = random.randint(1, 3)

    if number == 1:
        computer_choice = "Rock"
    elif number == 2:
        computer_choice = "Paper"
    elif number == 3:
        computer_choice = "Scissors"

    return computer_choice


def pick_winner():
    """Take both choices and compare to find the winner of the round"""

    game_round = 0
    while True:
        global user_score
        global comp_score

        comp = get_computer_choice()
        user = get_user_choice()

        # Test to see if user won, if not then computer wins
        if comp == user:
            print("\ntie\n")

        elif (
            comp == "Rock"
            and user == "Paper"
            or comp == "Paper"
            and user == "Scissors"
            or comp == "Scissors"
            and user == "Rock"
        ):
            print("\nPlayer wins\n")

            # When the user wins increment score
            user_score += 1
            print("User Score: " + str(user_score))
            print("Computer Score: " + str(comp_score))

        else:
            print("\nComputer wins\n")

            # When the computer wins increment score
            comp_score += 1
            print("User Score: " + str(user_score))
            print("Computer Score: " + str(comp_score))

        # Play 5 rounds and then stop loop
        if game_round == 4:
            if user_score > comp_score:
                print(
                    "\nUser has won this game with a score of "
                    + str(user_score)
                    + " points!\n"
                )
            else:
                print(
                    "\nThe computer has won this game with a score of "
                    + str(comp_score)
                    + " points!\n"
                )
            break

        #Increment round by 1
        game_round += 1


pick_winner()
