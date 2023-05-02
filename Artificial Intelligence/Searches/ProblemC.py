# Jack Carson
# Homework 1
# Problem C

import random

# Just run this program, you will be prompted for a state and the program will run until the goal state is reached!

def convertToList(state): # Helper function to convert the state to a list of integers
    string = str(state)
    stateList = []

    for i in range(len(string)):
        stateList.append(int(string[i]))
    
    return stateList

def moveState(state, action): # Helper function that takes a state and an action as input and returns the resulting state
    
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

    return str(''.join(map(str, stateList))) # Return the new state as an integer using the list of integers



# Part C --> Write a function(s) that makes random moves until the goal state is reached
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

def partC_goalState(state): # Checks if the state is a goal state
    one = int(str(state)[0] + str(state)[1] + str(state)[2])
    two = int(str(state)[3] + str(state)[4] + str(state)[5])    
    three = int(str(state)[6] + str(state)[7] + str(state)[8])    
    
    return True if one % 3 == 0 and two % 3 == 0 and three % 3 == 0 else False   

def partC_randomMoves(state): # Makes random moves until the goal state is reached, and prints the sequence of states and actions 
    while partC_goalState(state) == False:
        action = random.randint(1, 4)
        state = moveState(state, action)
        print(state, whichAction(action))
    
    print("Goal state reached!")
    print("Final state: ", state)
    
print("Problem C")

# ask the user for input and then run the program
user = ""
while len(user) != 9:
    user = input("Enter a 9 digit number: ")
    if len(user) != 9:
        if user == "exit":
            exit()
        print("Invalid input. Please try again.")
        user = ""
        
partC_randomMoves(user)
