from rpsfunctions import title, decideWinner, playerTie, playerWin, playerLoss, newgame
from random import choice

#-----------------------------------

playerLosses = 0
playerWins = 0
contplay = True
choices = ["rock", "paper", "scissors"]
options = ["y", "n", "yes", "no", "quit", "q"]

#-----------------------------------

title()
while True:

    newgame() #new game setup
    print(f'W: {playerWins} L: {playerLosses}')

#-----------------------------------

    comp = choice(choices)  # take user input and decide computer choice
    user = input("Enter your selection (rock/paper/scissors) >>> ").lower().strip()

    while user not in choices:
        if (user in ["quit","q"]): # fixing/rejecting typos or letting player quit
            print("Goodbye!")
            contplay = False
            break
        else:
            user = input(
                f"your input '{(user).lower()}' is not valid. Please try again. ").lower().strip()
    if contplay == False:
        break

#-----------------------------------

    print(f"\n\tuser: {user}") #print computer/user coiches
    print(f"\tcomputer: {comp}")

    winner = decideWinner(user, comp)  # call function to print win/lose/tie
    if winner:
        playerWins += 1 #track player wins/losses from decideWinner() return value
    elif winner == False:
        playerLosses += 1

#-----------------------------------

    playing = input("Thanks for playing! Would you like to play again? ").lower().strip()

    while playing not in options:
        playing = input(
            "Sorry, I don't understand. Would you like to play again? ").lower().strip()

    if (playing in ["yes","y"]):
        print("Okay! Let's play again!") #checking whether they want to play again
    elif (playing in ["no","n","q","quit"]):
        print("Goodbye!")
        break
    else:
        print("something went wrong...")
