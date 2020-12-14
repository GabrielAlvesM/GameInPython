from random import randint

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("U lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
            
    elif player == "Paper":
        if computer == "Sciessors":
            print("U lose!", computer, "cut", player)
        else:   
            print("U Win!", player, "covers", computer)
            
    elif player == "Scissors":
        if computer == "Rock":
            print("U Lose!", computer, "smashes", player)
        else:
            print("U Win!", computer, "cut", computer)
            
    else:
        print("Wrong word!")
        
    player = False
    computer = t[randint(0,2)]
        
            