""""
Programmer: Briton A. Powe          Program Homework Assignment #1
Date: 1/30/18                       Class: Introduction to A.I.
Version: 1.0.2
------------------------------------------------------------------------
Program Description:
Solves the Missionaries and Cannibals game using iterative deepening.
***This program uses Python 3.6.4***
"""

#Variables for start state, tracking path, and goal state
stateVector = [3,3,1]
path = []
goal = [0,0,0]

#Function to validate possible moves
def validateMoves(childState,validStates):
    numCannibals = 0
    numMissionaries = 0
    numCannibals = childState[1]
    numMissionaries = childState[0]
    numCannibals2 = 3 - numCannibals
    numMissionaries2 = 3 - numMissionaries
    if (numCannibals <= numMissionaries or 
        (numCannibals > 0 and numMissionaries == 0)):
        if (numCannibals2 <= numMissionaries2 or 
            (numCannibals2 > 0 and numMissionaries2 == 0)):
            if ((numCannibals >= 0 and numCannibals <= 3) and 
                (numMissionaries >= 0 and numMissionaries <= 3)):
                #if(path.__contains__(childState) == False):
                validStates.append(childState[:])

#Function to create moves based on current state
def createMoves(currentState):
    moves = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
    childState = [0,0,0]
    validStates = []

#Adding and Subtracting moves based on boat position
    for element in moves:
        if currentState [2] == 1:
            for i in range(3):
                childState [i] = currentState[i] - element[i]
        elif currentState [2] == 0:
            for i in range(3):
                childState [i] = currentState[i] + element[i]
        validateMoves(childState, validStates)
    return validStates

#Depth limited search part of iterative deepening algorithm
def depthLimitedSearch(stateVector, depth):
    path.append(stateVector)
    #print("Current Path: ",path)

    #If goal state is found, return the path
    if path.__contains__(goal):
        print("\n[!] Solution Found [!]\n")
        return path
    if depth > 0:
        childStates = createMoves(stateVector)
        for element in childStates:
            depthLimitedSearch(element,depth-1)
            if path.__contains__(goal):
                return path
            path.pop(len(path)-1)
        
    return []

#Main function for iterative deepening
def iterativeDeepening(stateVector):
    global path
    print("Searching...\n")
    for depth in range(999):
        tracedPath = depthLimitedSearch(stateVector, depth)

        #Pass successful path from depth first function
        if path.__contains__(goal):
            return path
        else:
            #Failed path is cleared
            path = []

#Print out results to terminal
def printResult(solution):
    print("Result Found at Depth",(len(solution)-1),"\n")
    print("Format:\t\t[Missionaries, Cannibals, Boat]\n")
    for index in range(len(solution)):
        print("State(",index,"):\t",solution[index])

#Main function calls
print("::Misionaries and Cannibals Solution Calculator::\n")
solution = iterativeDeepening(stateVector)
printResult(solution)
