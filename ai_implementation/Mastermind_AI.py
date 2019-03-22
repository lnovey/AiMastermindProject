# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:59:15 2019

@author: Anders Thuesen
"""
from collections import Counter
from itertools import product
import random


def evaluate(guess,secret_code):
    matches = sum((Counter(secret_code) & Counter(guess)).values())   
    
    correct_color = sum(i == j for i, j in zip(guess, secret_code))
    #zip command merge two lists into one.
    
    guessed_color = matches - correct_color
    
    return correct_color, guessed_color
  


def MAX_VALUE(guess,States):
           
    evaluation_list = []
    for i in range(len(States)):
        evaluation_list.append(evaluate(guess,States[i]))
        
    #This step counts the amount every score option occures for evaluation of the guess with all possible codes.
    evaluation_list_count = Counter(evaluation_list).values()

    MAX_count = max(evaluation_list_count)
    
    return MAX_count
    
    
#MAX_VALUE(All_Codes)

def MINIMAX(secret_code,All_Codes):
    #This function go through all the possible states with same evaluation as the previous guess and then select the ones with minimum amount of states.
    best_guess = "AABB"
    minimum = 1296
    States = All_Codes
    while True:
        feedback = evaluate(best_guess,secret_code)
        
        print("Guess {}: feedback {}".format(best_guess, feedback))
        if best_guess == secret_code:
            break
        States = [c for c in States if evaluate(best_guess, c) == feedback]
        print("States {}".format(States))
        print("Amount of states {}".format(len(States)))
        if len(States) == 1:
            best_guess = States[0]
        else:
            for i in range(len(States)):
                MAX_count = MAX_VALUE(States[i],States)
                if MAX_count < minimum:
                    minimum = MAX_count
                    best_guess = States[i]
                if States[i] == secret_code:
                    break
         
            
        print(best_guess)

All_Codes = [''.join(c) for c in product('ABCDEF', repeat=4)]

MINIMAX("EFCA",All_Codes)


