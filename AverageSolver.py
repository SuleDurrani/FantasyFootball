import pandas as pd
from printTeam import printOutput

pd.set_option('display.max_rows', 1000)
df = pd.read_csv(r'data.csv')


def bestAvg(position, playerCount):
    tempList = []
    avgC = 0  # average cost per player in this position
    counter = 0
    for i in range(len(df)):
        if df.loc[i][4] == position:
            tempList.append(
                [df.loc[i][0], df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4]])
            avgC += df.loc[i][3]
            counter += 1
    avgC = avgC / counter

    sortedList = sorted(tempList, key=lambda x: (x[2]), reverse=True)  # sort by index of each entry (based on points)
    returnedList = []
    for i in range(len(sortedList)):
        if sortedList[i][3] < avgC + avgC/2:
            # throw out any players who are more expensive than the average of that position * 1.5
            returnedList.append(sortedList[i])
    returnedList = returnedList[0:playerCount]
    return returnedList


def findBestAverage():
    print("--- Find best team relative to the average price in that position ---")

    outputList = [bestAvg("GK", 1), bestAvg("DEF", 4), bestAvg("MID", 4), bestAvg("FOR", 2)]
    outputList = [val for sublist in outputList for val in sublist]
    printOutput(outputList)

    d = pd.DataFrame(outputList, columns=["Player", "Team", "Points", "Cost", "Position"])
    d.to_csv('team2.csv', index=False)
