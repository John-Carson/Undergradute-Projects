# Jack Carson
# Homework 1
# Problem B

# Function call to move states is on line 42!

def convertToList(state): # Helper function that converts the input to a list of integers
    string = str(state)
    stateList = []

    for i in range(len(string)):
        stateList.append(int(string[i]))
    
    return stateList

# Part B --> Write a function that takes a state and an action as input and returns the resulting state
def moveState(state, action): 
    
    stateList = convertToList(state)
    index = stateList.index(0) # Get the index of the blank square
    
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
    
print("Part B: Move between states")  
  
part_b = print(moveState(724506831, 3)) # Returns 724056831, try other actions to see the results!