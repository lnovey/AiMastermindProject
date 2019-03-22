#Mastermind Board Game
import sys
import numpy as np
import Mastermind_AI as AI
import random

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")

# Game variables
colors = 'RBYGW'  # Allowed colors
#code = list(np.random.choice(colors, 4, replace=True)) # Generates random secret code with colors as only allowed colors.

code = ""
for i in range(0,4):
    code += random.choice(colors)



ai = False # deciding if it's AI or the user playing
game = True

attempts = 0
X = np.array([])


print("Secret color code = {}".format(code))

answer = input("Choose 1 to play yourself or 2 to watch the AI play: ")

if answer == '1':
    print("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W)")
    print("An example guess could be: GGBB")
    print("An 'X' in the reply means a correct colour in a correct place.")
    print("An 'O' in the reply means a correct colour in the wrong place.")
elif answer == '2':
    ai = True
    game = False
else:
    print("Wrong input.")
    sys.exit(-1)



while game:
    
#    correct_color = ""
#    guessed_color = ""
    print("Past tries:")
    print(X)

    if ai:
        pass
    else:
        guess = input("Attempt {}: ".format(attempts+1)).upper()
#        guess = guess.upper().replace(" ", "").split(",")

        if len(guess) != len(code):  # Criteria for correct player input
            print("Invalid Input")
            continue

        for i in range(len(code)):
            if guess[i] not in colors:
                print(guess[i] + " Is invalid input, not a possible color")
                continue

    # We have a problem here, if you put in the wrong input it still count is
    # as a attempt and stores it in the output matrix
    
        
        if guess == code:
            print("holy hell you did it in {} attempts".format(attempts+1))
            print(X)
            sys.exit(0)
            
        if attempts > 10:
            print("Sorry you didnt make it, you only have 10 attempts.")
            print("The correct color code was {}.".format(code))
            sys.exit(0)
            
        else:
            
            bulls, cows = evaluate(guess, code)
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
    All_Codes = [''.join(c) for c in product(colors, repeat=4)]
    print("Input a code for the computer to solve, eg. BWWG")
    code = input("Input code here: ").upper()
    AI.MINIMAX(code,All_Codes)
    

#The Output of the game will be vector X with shape (attempts,6)
#Column 4 is the amount of guesses you got correctly
#column 5 is the amount of colors you got correctly but placed wrong
