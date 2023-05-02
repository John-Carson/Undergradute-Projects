# Jack Carson
# Homework 1
# Problem A

import random
from itertools import permutations

def printPuzzle(array): # Prints the puzzle in a 3x3 grid
    print(array[0], array[1], array[2])
    print(array[3], array[4], array[5])
    print(array[6], array[7], array[8])
    print('\n')

# Part A --> Create a dictionary of all possible goal states, and print 10 random states
part_a = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8])) # All possible permutations

print("Part A: 10 random states")
for i in range(10):
    printPuzzle(part_a[random.randint(0, len(part_a))])
    
print("The size of the dictionary is: ", len(part_a)) # Size of the permutations list 

