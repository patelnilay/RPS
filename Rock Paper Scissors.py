#rock. paper. scissors. game made by Johnny

userScore = 0
#initialised user score variable
computerScore = 0
#initialised computer score variable
gamesPlayed = 0
#initialised games playes variable
computerPick = ""
#initialised computer's choice variable
userPick = ""
#initialised computer's choice variable
choices = ["rock","paper","scissors"]
# made a list for the computer to choose from
maxx = 3
#initialised games played max constant
import random
#importing module


while gamesPlayed < maxx:
    while userPick != "rock" or userPick != "paper" or userPick != "scissors":
        userPick = input("Pick Rock, Paper or Scissors: ").lower()
        if userPick == "rock" or userPick == "paper" or userPick == "scissors":
            break
#while loop to make sure user cannot input random entries to break the code
    print("You chose: ")
    print(userPick)
    print("  ")
    #print("userChoiceRan")#

#function for computer to choose randomly from list
    def computerPick():
        computerChoice = (random.choice(choices))#computer pick is now random
        return computerChoice

    compVal = computerPick() #computerPick function is called
    userVal = userPick #userPick is now assigned to userVal

    print("The Computer chose: ")
    print(compVal)
    #print("compVal called") #debug

#large if statement to check who wins
    if userVal == "rock" and compVal == "scissors":
        #print("debg-1")#debug
        print(" ")
        userScore += 1
    elif userVal == "scissors" and compVal == "paper":
        #print("debg-2")#debug
        print(" ")
        userScore +=1
    elif userVal == "paper" and compVal == "rock":
        #print("degbg-3")#debug
        print(" ")
        userScore +=1
    elif userVal == "scissors" and compVal == "rock":
        #print("debg-4")#debug
        print(" ")
        computerScore += 1
    elif userVal == "paper" and compVal == "scissors":
        #print("debg-5")#debug
        print(" ")
        computerScore +=1
    elif userVal == "rock" and compVal == "paper":
        #print("degbg-6")#debug
        print(" ")
        computerScore +=1
    elif userVal == compVal:
        print ("DRAW")
        print(" ")
        userScore = userScore
        computerScore = computerScore

#checking to see if the computer or the user has won (their score =3)
    if userScore == maxx:
        break
    print("Your Score")
    print (userScore)


    if computerScore == maxx:
        break
    print ("Computer Score =")
    print (computerScore)
    print(" ")


#print("broken") #debug

#win print statement
if userScore == 3:
    print("YOU WON!!")
elif computerScore == 3:
    print("YOU LOST BETTER LUCK NEXT TIME. :(")
