# Jack Carson
# Homework 1
# Problem D

from queue import Queue

# Uncomment the end of this program to view the different outputs!
# # of Actions Taken == Line 82
# States && Actions Taken == lines 84 && 85

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

# Part D --> Use BFS to solve the puzzle, and print the sequence of states and actions
def BFS(start, finish):
    closed = set() # Create open and closed lists
    openlist = Queue()
    openlist.put(start)
    
    actionlist = []
    actionlist.append(0)
    
    while not openlist.empty():
        current = openlist.get() 
        closed.add(current)
        
        for i in range(1, 5):
            child = moveState(current, i)
            if child not in closed and child not in openlist.queue:
                if child == finish:
                    print("Goal state reached!")
                    return closed, actionlist
                else: 
                    openlist.put(child)
                    actionlist.append(i)    

list = list(BFS("724506831", "012345678"))

# print("List length for BFS ", len(list[0])) # Uncomment for the number of actions taken

#for i in range(len(list[0])):
#    print("State: ", list[0].pop(), "Action: ", whichAction(list[1].pop())) # Uncomment to print the states and actions taken during BFS

# BFS Search 1 --> List length for BFS  158791
# BFS Search 2 --> List length for BFS  158791
# BFS Search 3 --> List length for BFS  158791

# After running the BFS search 3 times, the length of the list is on average 158791 states before the solution state is found