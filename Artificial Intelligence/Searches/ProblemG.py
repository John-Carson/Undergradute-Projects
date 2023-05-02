# Jack Carson 
# Homework 1
# Problem G

import random
from queue import Queue

# UNCOMMENT LINES 85 / 130 TO RUN EQUALLY WEIGHTED UCS OR WEIGHTED UCS RESPECTIVELY :)

def convertToList(state): # Converts the state to a list of integers
    string = str(state)
    stateList = []

    for i in range(len(string)):
        stateList.append(int(string[i]))
    
    return stateList

def moveState(state, action): # Moves the state based on the action taken
    
    stateList = convertToList(state)
    index = stateList.index(0)
    
    if action == 1: # Move up
        if index not in [0, 1, 2]:
            stateList[index], stateList[index - 3] = stateList[index - 3], stateList[index]
            
    elif action == 2: # Move down
        if index not in [6, 7, 8]:
            stateList[index], stateList[index + 3] = stateList[index + 3], stateList[index]
            
    elif action == 3: # Move left
        if index not in [0, 3, 6]:
            stateList[index], stateList[index - 1] = stateList[index - 1], stateList[index]
    
    elif action == 4: # Move right
        if index not in [2, 5, 8]:
            stateList[index], stateList[index + 1] = stateList[index + 1], stateList[index]

    return str(''.join(map(str, stateList))) # Return the new state as a string using the list of integers

def whichAction(action): # Prints the action that was taken
    if action == 0: # Move
        return "Start State"
    elif action == 1:
        return "Up"
    elif action == 2:
        return "Down"
    elif action == 3: 
        return "Left"
    elif action == 4:
        return "Right"
    else:
        return "Error"        

# Part G (G1) --> Use UCS to solve the puzzle, and print the sequence of states and actions
def Arbitrary_UCS(startState, goalState):    
    cost = 0
    action = 0
    closed = [] # Create open and closed lists
    
    State_Action_Cost_List = []
    State_Action_Cost_List.append([startState, action, cost])
    
    while State_Action_Cost_List:
        State_Action_Cost_List.sort(key = lambda x: x[2]) # sort the list by cost
        current = State_Action_Cost_List.pop(0)
        closed.append(current[0])
        
        print("Current State: ", current[0], "Action: ", whichAction(current[1]), "Cost: ", current[2]) # Uncomment to print the states and actions with cost

        for i in range(1, 5):
            child = moveState(current[0], i)
            if child not in closed and child not in [x[0] for x in State_Action_Cost_List]:
                if child == goalState:
                    print("Goal State Found!")
                    return closed
                else:
                    State_Action_Cost_List.append([child, i, current[2] + 1]) # Every cost has the same weight (current[2] + 1)

# Generate a random string with the characters 0-8
startState = ''.join(random.sample('012345678', 9))
finalState = "123804765"          

# search = Arbitrary_UCS(startState, finalState) UNCOMMENT ME TO RUN AN EQUALLY WEIGHTED UCS

# Using an arbitrary start state, the goal state may or may not be found (Below is an example of a found goal state at an early cost)
#Current State:  128043765 Action:  Down Cost:  16
#Current State:  123084765 Action:  Down Cost:  16
#Goal State Found!

# This equally weighted UCS is not optimal, and generally has the same performance as BFS (Priority Queue == Queue when all costs are equal) :D

# (G2)--> Use a Weighted UCS to solve the puzzle, and print the sequence of states and actions
def Weighted_UCS(startState, goalState):    
    cost = 0
    action = 0
    closed = [] # Create open and closed lists
    
    State_Action_Cost_List = []
    State_Action_Cost_List.append([startState, action, cost])
    
    while State_Action_Cost_List:
        State_Action_Cost_List.sort(key = lambda x: x[2]) # sort the list by cost
        current = State_Action_Cost_List.pop(0)
        closed.append(current[0])
        
        print("Current State: ", current[0], "Action: ", whichAction(current[1]), "Cost: ", current[2]) # Uncomment to print the states and actions with cost

        for i in range(1, 5):
            child = moveState(current[0], i)
            if child not in closed and child not in [x[0] for x in State_Action_Cost_List]:
                if child == goalState:
                    print("Goal State Found!")
                    return closed
                else:
                    if i == 1: # Up Cost
                        State_Action_Cost_List.append([child, i, current[2] + 1])
                    elif i == 2: # Down Cost
                        State_Action_Cost_List.append([child, i, current[2] + 1])
                    elif i == 3: # Left Cost
                        State_Action_Cost_List.append([child, i, current[2] + 2])
                    elif i == 4: # Right Cost
                        State_Action_Cost_List.append([child, i, current[2] + 0.5])
                        

weightedStart = ''.join(random.sample('012345678', 9))
weightedFinish = "123804765" 

# search = Weighted_UCS(weightedStart, weightedFinish) # UNCOMMENT ME TO RUN A WEIGHTED UCS

# Using an arbitrary start state, the goal state may or may not be found 
# I ran this 10 times, and the goal state was found 0 times at a cost of ~30 each search, so it is not optimal :(
# This is due to an asymmetric cost function, which is not optimal for UCS
# Performance is generally worse than BFS, and equally weighted UCS



                        
                        



