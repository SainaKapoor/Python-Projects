#Name: Saina Kapoor
#Student No.: 400433017
#Assignment 1
#A classic Rock, paper, scissor game with new members called SPock and Lizard

#Question:
#1. Write a python program for the Rock Paper Scissors Spock Lizard game. The rules of the game
#are:
#Spock beats scissors and rock, but loses to paper and lizard.
#Lizard beats Spock and paper, but loses to rock and scissors.
#Rock beats scissors and lizard, but loses to paper and Spock.
#Paper beats rock and Spock, but loses to scissors and lizard.
#Scissors beats paper and lizard, but loses to rock and Spock.
#The program will have two players and each of them produce a random outcome, i.e., Rock,
#paper, scissor, spock, or lizard. Based on each player’s outcome, determine the winner.


import random #importing random
game= ["Rock","Paper","Scissors", "Spock", "Lizard" ]

#Defining Player1 and Player2 variable to choose random object from game
player1 = random.choice(game)
player2 = random.choice(game)

#Printing what each player choice
print("Player 1 chose:", player1)
print("Player 2 chose:", player2)

#Checking for the conditions
if player1 == player2:
    print ("It's a tie")
    
elif player1 == "Spock":
    if (player2=="Scissors" or player2=="Rock"):
        print("Player1 wins")
    else:
        print("Player2 wins")
           
elif player1 == "Lizard":
    if (player2=="Spock" or player2=="Paper"):
       print("Player1 wins")
    else: 
       print("Player2 wins")

elif player1 == "Rock":
    if (player2=="Scissors" or player2=="Lizard"):
        print("Player1 wins")
    else: 
       print("Player2 wins")
        
elif player1 == "Paper":
    if (player2=="Rock" or player2=="Spock"):
        print("Player1 wins")
    else: 
       print("Player2 wins")
    
elif player1 == "Scissors":
    if (player2=="Paper" or player2=="Lizard"):
        print("Player1 wins")
    else: 
       print("Player2 wins")
        