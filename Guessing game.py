import random

computerGuess = random.randint(0,100)

while True:
    userGuess = int(input("Guess a number between 0 - 100 please:"))
    if userGuess > computerGuess:
        print("{Guess lower}")
    elif userGuess < computerGuess:
        print("{Guess higher}")
    else:
        print("You have guessed correctly!")
        
    if userGuess > 100:
        print("(Your guess must be 100 or less!)")
        
    if userGuess < 0:
        print("(Your guess must be 0 or more!)")
        break

    
 
