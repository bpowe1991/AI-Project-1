stateVector = [3,1,0]

def validateMoves(childState,validStates):
    numCannibals = 0
    numMissionaries = 0
    numCannibals = childState[1]
    numMissionaries = childState[0]
    numCannibals2 = 3 - numCannibals
    numMissionaries2 = 3 - numMissionaries
    if numCannibals <= numMissionaries or (numCannibals > 0 and numMissionaries == 0):
        if numCannibals2 <= numMissionaries2 or (numCannibals2 > 0 and numMissionaries2 == 0):
            if (numCannibals >= 0 and numCannibals <= 3) or (numMissionaries >= 0 and numMissionaries <= 3):
                validStates.append(childState[:])


def createMoves(currentState):
    moves = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
    childState = [0,0,0]
    validStates = []

    for element in moves:
        if stateVector [2] == 1:
            for i in range(3):
                childState [i] = currentState[i] - element[i]
        elif stateVector [2] == 0:
            for i in range(3):
                childState [i] = currentState[i] + element[i]
        validateMoves(childState, validStates)
    print("All States: ",validStates)

createMoves(stateVector)