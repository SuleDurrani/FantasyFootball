import pandas as pd
from printTeam import printOutput

pd.set_option('display.max_rows', 1000)
df = pd.read_csv(r'data.csv')


def bestPlayer(position, playerCount):
    tempList = []  # find the best team where the cost of every player is less than a set value
    for i in range(len(df)):
        if df.loc[i][4] == position:
            tempList.append([df.loc[i][0], df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4]])
    sortedList = sorted(tempList, key=lambda x: (x[2]), reverse=True)
    tl = []
    for i in range(len(sortedList)):
        if sortedList[i][3] < 10.5:  # this is the cost that gets the highest valued team returned
            tl.append(sortedList[i])
    returnedList = tl[0:playerCount]
    return returnedList


def findHighestPointsWithinEqualCost():
    print("--- Find best points for each position relative to a set price for all positions ---")
    outputList = [bestPlayer("GK", 1), bestPlayer("DEF", 4), bestPlayer("MID", 4), bestPlayer("FOR", 2)]
    outputList = [val for sublist in outputList for val in sublist]
    printOutput(outputList)

    d = pd.DataFrame(outputList, columns=["Player", "Team", "Points", "Cost", "Position"])
    d.to_csv('team3.csv', index=False)
