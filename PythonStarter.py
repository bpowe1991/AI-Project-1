stateVector = [1,1,1]
moves = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
childState = [0,0,0]
allStates = []
numCannibals = 0
numMissionaries = 0
for element in moves:
    print("Element: ",element)
    if stateVector [2] == 1:
        for i in range(3):
            childState [i] = stateVector[i] - element[i]
        print("Child: ",childState)
    elif stateVector [2] == 0:
        for i in range(3):
            childState [i] = stateVector[i] + element[i]
        print("Child: ",childState)
    numCannibals = childState[1]
    numMissionaries = childState[0]
    numCannibals2 = 3 - numCannibals
    numMissionaries2 = 3 - numMissionaries
    if numCannibals <= numMissionaries or (numCannibals > 0 and numMissionaries == 0):
        if numCannibals2 <= numMissionaries2 or (numCannibals2 > 0 and numMissionaries2 == 0):
            if (numCannibals >= 0 and numCannibals <= 3) or (numMissionaries >= 0 and numMissionaries <= 3):
                allStates.append(childState[:])
print("All States: ",allStates)

