# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:21:37 2019

@author: Anders Thuesen
"""

#Mastermind Board Game

import random
import numpy as np

print (" --- MASTERMIND --- \n")
print ("Guess the secret color code in as few tries as possible.\n")
print ("Please, enter your color code.\nYou can use red(R), green(G), blue(B), yellow(Y)")
print("Seperate the colors witb comma e.g R,B,Y,G.")
print("Important to input correctly because if not it fucks up the attempt number. \n")

#Allowed colors
colors = ['R','B','Y','G']

#Generates random secret code with colors as only allowed colors.
color_code = list(np.random.choice(colors,4,replace=True))
    
print("Secret color code = " + str(color_code))

game = True

attempts = 0


X = np.array([])

while game:
    
    correct_color = ""
    guessed_color = ""
    print("Past tries:")
    print(X)
    
    players_guess = input("Attempt "+str(attempts+1)+":").upper()
    players_guess = players_guess.split(",")
    attempts +=1
    

    
    #Criteria for correct player input


    if len(players_guess) != len(color_code):
        print("Invalid Input")
        attempts -=1
        continue 
    
    for i in range(len(color_code)):
        if players_guess[i] not in colors:
            print(players_guess[i]+" Is invalid input, not a possible color")
            continue
    
    
    
    if players_guess == color_code:
        print("holy hell you did it in "+str(attempts)+" attempts")
        print(X)
        game = False
        
    if attempts > 5:
        print("Sorry you didnt make it, you only have 5 attempts.")
        print("The correct color code was " + str(color_code))
        game = False
        
    if attempts <=5:
        
        for i in range(len(color_code)):
            if players_guess[i] == color_code[i]:
                correct_color += "X"
                
        for i in range(len(color_code)):     
            if players_guess[i] != color_code[i] and players_guess[i] in color_code: 
                if len(correct_color)+len(guessed_color) <= color_code.count(players_guess[i]):
                    
                    guessed_color += "O"
                else:
                    continue
                
                
                
        print(correct_color +" "+guessed_color)
        
    
    players_guess = np.array(players_guess)
    players_guess = np.append(players_guess,len(correct_color))
    players_guess = np.append(players_guess,len(guessed_color))   
    X = np.append(X,np.array(players_guess))
    
    X = np.reshape(X,(attempts,6))

 

#The Output of the game will be vector X with shape (attempts,6) 
#Column 4 is the amount of guesses you got correctly
#column 5 is the amount of colors you got correctly but placed wrong
