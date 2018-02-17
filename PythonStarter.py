stateVector = [3,3,1]
moves = [[1,0,1],[2,0,1],[0,1,1],[0,2,1],[1,1,1]]
childState = [0,0,0]
allStates = []
for element in moves:
    print("Element: ",element)
    if stateVector [2] == 1:
        for i in range(2):
            childState [i] = stateVector[i] - element[i]
        print("Child: ",childState)
    elif stateVector [2] == 0:
        for i in range(2):
            childState = stateVector[i] + element[i]
    allStates.append(childState[:])
print("All States: ",allStates)

        