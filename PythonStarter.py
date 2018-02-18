stateVector = [3,3,1]
path = []
goal = [0,0,0]

def validateMoves(childState,validStates):
    numCannibals = 0
    numMissionaries = 0
    numCannibals = childState[1]
    numMissionaries = childState[0]
    numCannibals2 = 3 - numCannibals
    numMissionaries2 = 3 - numMissionaries
    if numCannibals <= numMissionaries or (numCannibals > 0 and numMissionaries == 0):
        if numCannibals2 <= numMissionaries2 or (numCannibals2 > 0 and numMissionaries2 == 0):
            if (numCannibals >= 0 and numCannibals <= 3) and (numMissionaries >= 0 and numMissionaries <= 3):
                #if(path.__contains__(childState) == False):
                validStates.append(childState[:])


def createMoves(currentState):
    moves = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
    childState = [0,0,0]
    validStates = []

    for element in moves:
        if currentState [2] == 1:
            for i in range(3):
                childState [i] = currentState[i] - element[i]
        elif currentState [2] == 0:
            for i in range(3):
                childState [i] = currentState[i] + element[i]
        validateMoves(childState, validStates)
    return validStates


def depthLimitedSearch(stateVector, depth):
    path.append(stateVector)
    print("Current Path: ",path)
    if path.__contains__(goal):
        print("Found!")
        return path
    if depth > 0:
        childStates = createMoves(stateVector)
        for element in childStates:
            depthLimitedSearch(element,depth-1)
            if path.__contains__(goal):
                return path
            path.pop(len(path)-1)
        
    return []


def iterativeDeepening(stateVector):
    global path
    for depth in range(12):
        print("Iterative Deep level: ", depth)
        tracedPath = depthLimitedSearch(stateVector, depth)
        if path.__contains__(goal):
            return path
        else:
            print("Failed to Find at Depth",depth)
            path = []


def printResult(solution):
    print("Result Found at Depth",(len(solution)-1))
    for index in range(len(solution)):
        print("State(",index,"):\t",solution[index])

solution = iterativeDeepening(stateVector)
printResult(solution)
