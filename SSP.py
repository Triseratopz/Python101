import random
import os

isRunning = True
computerWins = 0
playerWins = 0

#Best of of three
while isRunning:
    
    if computerWins == 3:
        
        print  ("GAME OVER! Computer is the champ!")
        isRunning = False
        break
        

    if playerWins == 3:
        
        print ("GLORIOUS VICTORY! Player wins!")
        isRunning = False
        break
        

      



    print ("---------------------------------------")
    print ("ROCK, PAPER, SCISSORS")
    print ("---------------------------------------")
    print ("Score: Player " + str(playerWins) + " Computer: " + str(computerWins) )
    print ("---------------------------------------")

    print ("Make your choice: ")
    print ("1. Rock")
    print ("2. Paper")
    print ("3. Scissors ")

    playerMove = int (input("Hva velger du: "))
        
    computerMove = random.randint(1, 3)

    os.system('CLS')
        


    if computerMove == playerMove:
        
        print ("Draw, you made the same move. Try again.")
    elif computerMove == 1 and playerMove == 2:
        
        print ("Player wins, paper beats rock!")
        playerWins += 1
        
    elif computerMove == 1 and playerMove == 3:
        
        print ("Computer wins, rock beats scissors!")
        computerWins+= 1
        
    elif computerMove == 2 and playerMove == 1:
        
        print ("Computer wins, paper beats rock!")
        computerWins += 1
        
    elif computerMove == 2 and playerMove == 3:
        
        print ("Player wins, scissors beats paper")
        playerWins += 1
    elif computerMove == 3 and playerMove == 1:
        
        print ("Player wins, rock beats scissors")
        playerWins += 1
    elif computerMove == 3 and playerMove == 2:
        
        print ("Computer wins, scissors beats paper")
        computerWins += 1
        