import sys
import random

list = ["rock", "paper", "scissors"]

playerOne = input("What's your name? ")
playerAnswer = input(
    "%s, Do you want to choose rock, paper or scissors: " % playerOne)
computer = random.choice(list)


def compare(p1, p2):
    if p1 == p2:
        return ("It's a tie!")
    elif p1 == 'rock':
        if p2 == 'scissors':
            return(playerOne, "wins!")
        else:
            return("Computer wins!")

    elif p1 == 'scissors':
        if p2 == 'paper':
            return(playerOne, 'wins!')
        else:
            return("Computer wins!")

    elif p1 == 'paper':
        if p2 == 'rock':
            return(playerOne, 'wins!')
        else:
            return("Computer wins!")

    else:
        return("invalid input!")
        sys.exit()


print(compare(playerAnswer, computer))
