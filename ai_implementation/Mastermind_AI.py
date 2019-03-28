from collections import Counter
from itertools import product


def evaluate(guess,code):
    #This is the evaluation function that evaluate the guess to another code
    #It returns the amount of bulls and cows. 
    #Finding all the matches
    All_matches = sum((Counter(code) & Counter(guess)).values())   
    #Finding the bulls, the correct color and correct placement
    bulls = sum(i == j for i, j in zip(guess, code))
    #Cows is thus    
    cows = All_matches - bulls
    
    return bulls, cows
  


def MAX_VALUE(guess,States):
    #The purpose of this function is to evaluate the guess to all the possible states
    #and then return the score (bulls and cows) that is the most occurent.      
    #Evaluation_list is being filled with all evaluations with respect to the guess.
    evaluation_list = []
    for i in range(len(States)):
        evaluation_list.append(evaluate(guess,States[i]))  
    #This step counts the amount every score option occures in evaluation_list.
    evaluation_list_count = Counter(evaluation_list).values()
    #Taking the max score. 
    MAX_count = max(evaluation_list_count)
    
    return MAX_count
    
    
#MAX_VALUE(All_Codes)

def MINIMAX(code,All_Codes):
    #This function go through all the possible states with same evaluation as the previous guess
    #and then select the best guess based on the one with the smallest amount of states.
    #Best initial guess is found from earler investigations with the AI 
    best_guess = "YYRR"
    minimum = len(All_Codes)
    States = All_Codes
    guess_count = 1
    while True:
        #Evaluate the guess to the secret code
        eval_guess = evaluate(best_guess,code)
        print("AI's guess nr. {}: Guess {}. Bulls and Cows: {}".format(guess_count, best_guess,eval_guess))
        #Terminal test to break the loop if the guess is correct.
        if best_guess == code:
            print("The AI have guessed the secret code {} in {} tries".format(code,guess_count))
            break
        
        #This step removes the states that do not have the same evaluation as eval_guess
        States = [i for i in States if evaluate(best_guess, i) == eval_guess]
        print("{} states have similar evaluation: {}".format(len(States),States))
        
        if len(States) == 1:
            best_guess = States[0]
            
        #Loops through the possible states and take the one with the min-max value. 
        else:
            for i in range(len(States)):
                MAX_count = MAX_VALUE(States[i],States)
                if MAX_count < minimum:
                    minimum = MAX_count
                    best_guess = States[i]
                if States[i] == code:
                    break
                                    
        guess_count += 1  
