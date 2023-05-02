# Jack Carson
# Homework 1
# Problem E

# Uncomment line 78 for the length of the closed list, and lines 80 && 81 for the states and actions taken

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

# Part E --> Use DFS to solve the puzzle, and print the sequence of states and actions
def DFS(start, finish):
    
    openlist = []
    closed = set()
    openlist.append(start)
    
    actionlist = []
    actionlist.append(0)
    
    while openlist: # While the list is not empty
        current = openlist.pop() 
        closed.add(current)
        for i in range(1, 5):
            child = moveState(current, i)
            if child not in closed and child not in openlist:
                if child == finish:
                    print("Goal state reached!")
                    return closed, actionlist
                else: 
                    openlist.append(child) 
                    actionlist.append(i)   

list = list(DFS("724506831", "012345678"))

# print("List length for DFS ", len(list[0])) # Uncomment for the number of actions taken

#for i in range(len(list[0])):
#    print("State: ", list[0].pop(), "Action: ", whichAction(list[1].pop())) # Uncomment to print the states and actions taken during DFS

# DFS Search 1 --> List length for DFS  54091
# DFS Search 2 --> List length for DFS  54091
# DFS Search 3 --> List length for DFS  54091

# Using a rough estimate, it takes about 54,091 actions to solve the puzzle using DFS
# When using BFS (Which averaged 158791 states to find the solution), DFS is much more efficient in terms of space complexity
# This is because using a stack keeps less states in memory than a queue, which is used in BFS O(mn) vs O(b^d) 

# Other factors to consider are the number of states in this problem, the depth of the tree, and the branching factor, all of which differ from problem to problem :)


