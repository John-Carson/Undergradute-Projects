# Jack Carson
# Homework 1
# Problem D

from queue import Queue

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

# Part F --> Use BFS to solve the clockwise puzzle, and print the sequence of states and actions
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
                    return closed
                else: 
                    openlist.put(child)
                    actionlist.append(i)    

# check if list is empty, if not, print the list, else print "No solution"
list = BFS("123456780", "123804765") # Call the BFS function for the clockwise puzzle

def printList(list):
    if list:
        for i in list:
            print(i)
    else:
        print("No solution")

printList(list)

# print("List length for BFS ", len(states)) # Uncomment for the number of actions taken (Will be of length 0, as the goal state is not added to the list)

# BFS Search 1 --> List length for BFS  (None)
# BFS Search 2 --> List length for BFS  (None)
# BFS Search 3 --> List length for BFS  (None)

# After running the BFS search 3 times searching for the clockwise solution...
# The solution is unable to be found. This is because the BFS search is not able to find the solution in a reasonable amount of time, using a reasonable amount of memory. 
# The function then returns an empty list, which is then printed as "No solution".