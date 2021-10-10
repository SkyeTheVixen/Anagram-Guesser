#Import the random function
from random import random

sPlaying = "y"
iScore = 0

while(sPlaying == "y"):
    #Generate a pseudo random number by generating a random number between 0 and 1, then multiplying by the total, then rounding it
    iRandomNumber = round(random()*20)-1

    #Open the file, split the file into lines as an array
    sLines = open("words.txt", "r").read().splitlines()

    #Split the line we select into two parts
    sResult = sLines[iRandomNumber].split(',')

    #Set the unscrambled word as the first entry
    sUnscrambledWord = sResult[0]
    #Set the scrambled word as the second entry
    sScrambledWord = sResult[1]

    #Print the users word to unscramble
    print("Your word: " + sScrambledWord)

    #Guess and score counter
    iGuesses = 1

    #Get users input while it doesnt match the unscrambled word
    sUserInput = input("Guess " + str(iGuesses) + ": ")

    #While the users input is not correct
    while (sUserInput != sUnscrambledWord):
        #increase guesses by 1
        iGuesses += 1
        #if they exceed max guesses then end
        if(iGuesses == 4):
            print("Game Over")
            iPlaying = input("Would you like to play again? (enter y to continue)")
            if(iPlaying != "y"):
                break
        #else ask for guess
        sUserInput = input("Guess " + str(iGuesses) + ": ")

    #If user input is correct
    if(sUserInput == sUnscrambledWord):
        print("Correct")
        #increase score
        iScore = iScore + 1
        #output score
        print("Your score is now: " + str(iScore))
        iPlaying = input("Would you like to play again? (enter y to continue)")
        if(iPlaying != "y"):
            break

print("Your final score is: " + str(iScore))
sUserName = input("Name: ")
open("scores.txt", "a").write("\n" + sUserName + ": " + str(iScore))


