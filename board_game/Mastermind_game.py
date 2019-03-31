#Mastermind Board Game
import sys
import numpy as np
from collections import Counter
from itertools import product
import ai_implementation.Mastermind_AI as AI
import random


ai = False # deciding if it's AI or the user playing
game = True

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")

answer = input("Choose 1 to play yourself or 2 to watch the AI play: ")

if answer == '1':
    print("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W), purple(P)")
    print("An example guess could be: GGBB")
    print("An 'X' in the reply means a correct colour in a correct place.")
    print("An 'O' in the reply means a correct colour in the wrong place.")
elif answer == '2':
    ai = True
    game = False
else:
    print("Wrong input.")
    sys.exit(-1)




colors = 'RBYGWP'  # Allowed colors

#Generating random secret code
code = ""
for i in range(0,4):
    code += random.choice(colors)
X = np.array([])   
attempts = 0

while game:
    print("Past tries:")
    print(X)
    print("Possible colors: {}".format(colors))
    if ai:
        pass
    else:
        guess = input("Attempt {}: ".format(attempts+1)).upper()
        
        if len(guess) != len(code):  # Criteria for correct player input
            print("Invalid Input")
            continue

        for i in range(len(guess)):
            if guess[i] not in colors:
                print("{} Is invalid input, not a possible color".format(guess[i]))
                continue

    # We have a problem here, if you put in the wrong input it still count is
    # as a attempt and stores it in the output matrix
    
        
        if guess == code:
            print("Congratulations you did it in {} attempts".format(attempts+1))
            print(X)
            break
            
        if attempts > 10:
            print("Sorry you didnt make it, you only have 10 attempts.")
            print("The correct color code was {}.".format(code))
            break
        else:           
            bulls, cows = AI.evaluate(guess, code)
            reply = []
            reply.append(["X" for _ in range(bulls)])
            reply.append(["O" for _ in range(cows)])
            print(reply)
    
        
        guess = np.array(guess)
        guess = np.append(guess, bulls)
        guess = np.append(guess, cows)
    
        X = np.append(X, np.array(guess))
        X = np.reshape(X,(attempts+1, 3))
    
        attempts += 1

if ai == True:
    #Defining all possbile states
    All_Codes = [''.join(i) for i in product(colors, repeat=4)]
    print("Input a code for the computer to solve, eg. BWWG.")
    print("Possible colors {}".format(colors))
    code = input("Input code here: ").upper()
    #Here we load in the AI.
    AI.MINIMAX(code,All_Codes)
    

#The Output of the game will be vector X with shape (attempts,6)
#Column 4 is the amount of guesses you got correctly
#column 5 is the amount of colors you got correctly but placed wrong
