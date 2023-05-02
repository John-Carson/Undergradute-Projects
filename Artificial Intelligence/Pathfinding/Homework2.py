# Jack Carson Homework 2
# CPSC 4420 - Artificial Intelligence
# 10/2/2022

import numpy as np # Numpy is the only library required
        
conversion = { 
    "00": [1,5], "01": [2,5], "02": [3,5], "03": [4,5], "04": [5,5], 
    "10": [1,4], "11": [2,4], "12": [3,4], "13": [4,4], "14": [5,4],
    "20": [1,3], "21": [2,3], "22": [3,3], "23": [4,3], "24": [5,3],
    "30": [1,2], "31": [2,2], "32": [3,2], "33": [4,2], "34": [5,2],
    "40": [1,1], "41": [2,1], "42": [3,1], "43": [4,1], "44": [5,1]
} # Converts between the two coordinate systems () (I used a differnt reference coordinate system, sorry for the confusion)

def get_agent_string(agent): # Helper function to get string
    string = ""
    for i in agent:
        string += str(i)
    return string

def get_agent_tuple(agent): # Helper function to get tuple
    agent = list(agent)
    for i in range(len(agent)):
        agent[i] = int(agent[i])
    return tuple(agent)
        
def format_coordinates(agent): # Format the coordinates to be printed
    string = get_agent_string(agent)
    if string[0:2] in conversion:
        new = conversion[string[0:2]] + [string[2]]
    return get_agent_tuple(new)  
        
States_Actions = { # Dictionary with states as keys, and actions as values
"001" : [], "002" : [3,4],  "003" : [], "004" : [3], "101" : [3], "102" : [3,4], "103" : [], "104" :[3,4], 
"201" : [3,4], "202" : [3,4], "203" : [], "204" : [], "301": [3,4], "302" : [3], "303" : [], "304" : [],  
"401" : [3,4], "402" : [], "403" : [], "404" : [3,4], "011" : [], "012": [3], "013": [3], "014" : [], 
"111" : [3], "112" : [], "113" : [3], "114" : [3,4], "411" : [], "412" : [], "413" : [3], "414": [3,4],
"021" : [], "022" : [3,4], "023" : [], "024" : [3,4], "121" : [3], "122": [3], "123" : [3,4], "124" : [3,4],
"221" : [3,4], "222" : [], "223" : [], "224" : [3,4], "421" : [], "422" : [], "423" : [3,4], "424": [3,4],    
"031" : [], "032" : [3,4], "033" : [3], "034" : [3], "231" : [3,4], "232" : [3,4], "233": [3], "234" : [3], 
"331" : [3,4], "332" : [3], "333" : [], "334": [3], "431" : [3,4], "432" : [], "433": [3,4], "434" : [3], 
"141" : [3], "142" : [], "143" : [3,4], "144" : [], "241" : [], "242": [3,4], "243" : [3,4], "244" : [], 
"341" : [3], "342": [3], "343" : [3], "344" : [], "441" : [3,4], "442" : [], "443" : [3,4], "444" : [],
"131": [], "132" : [], "133" : [], "134" : [], "041" : [], "042" : [], "043" : [], "044" : []
} 

for i in States_Actions: # Add move left and right as actions to all states
    States_Actions[i].append(1)
    States_Actions[i].append(2)

for i in States_Actions.keys(): # Remove actions from the end states
    if i[0:2] == "04":
        States_Actions[i].remove(1)
        States_Actions[i].remove(2)
    elif i[0:2] == "13":
        States_Actions[i].remove(1)
        States_Actions[i].remove(2)

States = [] # List of Tuples
for s in States_Actions: 
    States.append(get_agent_tuple(s))

Formatted_States = []
for s in States: # Format the states to be printed
    Formatted_States.append(format_coordinates(s))

Rewards = {} # Dictionary with states as keys, and rewards as values
for i in States: 
    if get_agent_string(i)[0:2] == "13":
        Rewards[get_agent_tuple(i)] = -10
    elif get_agent_string(i)[0:2] == "04":
        Rewards[get_agent_tuple(i)] = 1
    else: 
        Rewards[get_agent_tuple(i)] = 0
        
Actions_List = []
for i in States_Actions.values():
    Actions_List.append(tuple(i))
Actions = dict(zip(States, Actions_List)) # Dictionary of States and Actions
for i in range(8): # Remove Goal States from Action Dictionary
    Actions.popitem()

Policy = {} # Define a random policy for each state at the start
for i in Actions.keys(): 
    Policy[i] = Actions[i][np.random.randint(0, len(Actions[i]))]
        
V = {} # Define a value for each state at the start
for s in States:
    if get_agent_string(s)[0:2] == "13":
        V[get_agent_tuple(s)] = -10
    elif get_agent_string(s)[0:2] == "04":
        V[get_agent_tuple(s)] = 1
    else: 
        V[get_agent_tuple(s)] = 0
        
def turn_left(agent): # (Counter-Clockwise)
    agent = list(agent)
    if 1 in States_Actions[get_agent_string(agent)]: 
        if agent[2] == 1: # Turn Left From Up
            agent[2] = 3
        elif agent[2] == 2: # Turn Right From Down
            agent[2] = 4
        elif agent[2] == 3: # Turn Down From Left
            agent[2] = 2
        else:
            agent[2] = 1 # Turn Up From Right
        return get_agent_tuple(agent)
    else:
        return get_agent_tuple(agent)

def turn_right(agent): # (Clockwise)
    agent = list(agent)
    if 2 in States_Actions[get_agent_string(agent)]: 
        if agent[2] == 1: # Turn Right From Up
            agent[2] = 4
        elif agent[2] == 2: # Turn Left From Down
            agent[2] = 3
        elif agent[2] == 3: # Turn Up From Left
            agent[2] = 1
        else:
            agent[2] = 2 # Turn Down From Right
        return get_agent_tuple(agent)
    else: 
        return get_agent_tuple(agent)

def move_one(agent): # Move one cell forward
    agent = list(agent)
    for i in range(len(agent)):
        agent[i] = int(agent[i])
    if 3 in States_Actions[get_agent_string(agent)]:
        if agent[2] == 1: # Move Up
            agent[0] -= 1
        elif agent[2] == 2: # Move Down
            agent[0] += 1
        elif agent[2] == 3: # Move Left
            agent[1] -= 1
        else:
            agent[1] += 1 # Move Right
        return get_agent_tuple(agent)
    else:
        return get_agent_tuple(agent)
        
def move_two(agent): # Move two cells forward
    agent = list(agent)    
    for i in range(len(agent)):
        agent[i] = int(agent[i])
    if 4 in States_Actions[get_agent_string(agent)]:
        if agent[2] == 1: # Move Up
            agent[0] -= 2
        elif agent[2] == 2: # Move Down
            agent[0] += 2
        elif agent[2] == 3: # Move Left
            agent[1] -= 2
        else:
            agent[1] += 2 # Move Right
        return get_agent_tuple(agent)
    else: 
        return get_agent_tuple(agent)

# VALUE ITERATION ALGORITHM
def value_iteration(States, Rewards, Actions, Policy, V, Gamma, Noise): 
    iteration = 0
    while True: 
        for s in States: # Loop through all states
            if s in Policy: # If the state is not a goal state
                newValue = 0
                
                for a in Actions[s]: # Loop through all actions in the state
                    if a == 1: 
                        next = turn_left(s)
                    if a == 2: 
                        next = turn_right(s)
                    if a == 3: 
                        next = move_one(s)
                    if a == 4:
                        next = move_two(s)
                        
                    Random = np.random.choice([i for i in Actions[s] if i != a]) # Choose a random action
                    if Random == 1: 
                        nextRandom = turn_left(s)
                    if Random == 2:
                        nextRandom = turn_right(s)
                    if Random == 3:
                        nextRandom = move_one(s)
                    if Random == 4:
                        nextRandom = move_two(s)
                        
                    if Rewards[s] == 0: # Define the reward for the state if it is not a goal state
                        if a == 1 or a == 2: 
                            Rewards[s] = -0.005
                        elif a == 2:
                            Rewards[s] = -0.015
                        else:
                            Rewards[s] = -0.02
                        
                    Val =  Rewards[s] + (Gamma * ((1-Noise)* V[next] + (Noise * V[nextRandom]))) # Bellman Equation
                    if Val > newValue: # Save the action with the highest value
                        newValue = Val
                        Policy[s] = a
                    
                V[s] = newValue # Update the value of the state
        
        if iteration < 10:  # Format first 10 iterations
            print("\nIteration: ", iteration + 1)
            for i in States:
                if i not in Policy:
                    Action = str(0)
                if i in Policy:
                    Action = str(Policy[i])
                print("State ", str(format_coordinates(i)) + "\tV = " + str(round(V[i],3)), "\tBest Action: A" + Action)
        if iteration == 100:
            return V
        iteration += 1

def Part_B(): 
    B = value_iteration(States, Rewards, Actions, Policy, V, 1, 0)

# Part_B()

def Part_D(): 
    D = value_iteration(States, Rewards, Actions, Policy, V, 0.8, 0)

# Part_D()

def Part_E(): 
    E = value_iteration(States, Rewards, Actions, Policy, V, 0.2, 0)
    
# Part_E()