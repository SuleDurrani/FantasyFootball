import pandas as pd
from printTeam import printOutput

pd.set_option('display.max_rows', 1000)
df = pd.read_csv(r'data.csv')


def findOptimal(position, playerCount):
    tempList = []
    for i in range(len(df)):
        if df.loc[i][4] == position:
            tempList.append([df.loc[i][0], df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4]])

    sortedList = sorted(tempList, key=lambda y: (y[2] / y[3]), reverse=True)
    sortedList = sortedList[0:playerCount]
    return sortedList


def optimalPlayers():
    # attempt to find players with highest point to cost ratio
    print("--- Optimal price cost ratio ---")

    outputList = [findOptimal("GK", 1), findOptimal("DEF", 4), findOptimal("MID", 4), findOptimal("FOR", 2)]
    outputList = [val for sublist in outputList for val in sublist]

    printOutput(outputList)

    d = pd.DataFrame(outputList, columns=["Player", "Team", "Points", "Cost", "Position"])
    d.to_csv('team1.csv', index=False)
