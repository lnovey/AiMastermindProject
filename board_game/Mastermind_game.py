# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:21:37 2019

@author: Anders Thuesen
"""

#Mastermind Board Game
import sys
import numpy as np
from ai_implementation.minimax import evaluate, knuth

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")

# Game variables
colors = ['R','B','Y','G', 'W']  # Allowed colors
code = list(np.random.choice(colors, 4, replace=True)) # Generates random secret code with colors as only allowed colors.
ai = False # deciding if it's AI or the user playing
game = True
attempts = 0

print("Secret color code = " + str(code))

answer = input("Choose 1 to play yourself or 2 to watch the AI play: ")

if answer == '1':
    print("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y), white(W)")
    print("Separate the colors with comma e.g R,B,Y,G.\n")
    print("An 'X' in the reply means a correct colour in a correct place.")
    print("An 'O' in the reply means a correct colour in the wrong place.")
elif answer == '2':
    ai = True
else:
    print("Wrong input.")
    sys.exit(-1)




X = np.array([])

while game:
    
    correct_color = ""
    guessed_color = ""
    print("Past tries:")
    print(X)

    if ai:
        pass
    else:
        guess = input("Attempt {}: ".format(attempts+1))
        guess = guess.upper().replace(" ", "").split(",")
    attempts +=1
    

    
    #Criteria for correct player input


    if len(guess) != len(code):
        print("Invalid Input")
        attempts -=1
        continue 
    
    for i in range(len(code)):
        if guess[i] not in colors:
            print(guess[i] + " Is invalid input, not a possible color")
            continue
    
    
    
    if guess == code:
        print("holy hell you did it in "+str(attempts)+" attempts")
        print(X)
        game = False
        
    if attempts > 5:
        print("Sorry you didnt make it, you only have 5 attempts.")
        print("The correct color code was " + str(code))
        game = False
        
    if attempts <=5:
        
        bulls, cows = evaluate(guess, code)
        reply = []
        reply.append(["X" for _ in range(bulls)])
        reply.append(["O" for _ in range(cows)])
        print(reply)

    
    guess = np.array(guess)
    guess = np.append(guess, len(correct_color))
    guess = np.append(guess, len(guessed_color))
    X = np.append(X, np.array(guess))
    
    X = np.reshape(X,(attempts,6))

 

#The Output of the game will be vector X with shape (attempts,6) 
#Column 4 is the amount of guesses you got correctly
#column 5 is the amount of colors you got correctly but placed wrong
