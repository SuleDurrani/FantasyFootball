def printOutput(outputList):
    totalPoints = 0
    totalCost = 0.0
    print(outputList)
    for i in range(len(outputList)):
        totalPoints += outputList[i][2]
        totalCost += outputList[i][3]

    print("Total points: " + str(totalPoints))
    print("Total cost: " + str(totalCost))
