import time
import random
import pandas as pd

pd.set_option('display.max_rows', 1000)
df = pd.read_csv(r'data.csv')


def bogoCreateTeam(GKList, DEFList, MIDList, FORList, highest):
    tempList = [random.choice(GKList)]
    for i in range(4):
        temp = random.choice(DEFList)
        if temp not in tempList:
            tempList.append(temp)
    for i in range(4):
        temp = random.choice(MIDList)
        if temp not in tempList:
            tempList.append(temp)
    for i in range(2):
        temp = random.choice(FORList)
        if temp not in tempList:
            tempList.append(temp)

    totalPoints = 0
    totalCost = 0
    for i in range(len(tempList)):
        totalPoints += tempList[i][2]
        totalCost += tempList[i][3]

    totalCost = totalCost

    if totalPoints > highest and totalCost <= 83.8:
        global bogoList
        bogoList = tempList
        print("Total cost: " + "{:.1f}".format(totalCost) + ", Total points: " + str(totalPoints))
        return totalPoints

    else:
        return highest


def sortList(li):
    li = sorted(li, key=lambda y: (y[2]), reverse=True)
    li = li[:8]
    return li


def bogoTeamFinder(minutes):
    print("--- Algorithm that creates a random team, and checks if it is better than the previous best team ---")
    print("--- This will run for %s minute/s ---" % minutes)

    playerList = df.values.tolist()
    GKList, DEFList, MIDList, FORList = [], [], [], []

    for i in range(len(playerList)):
        if playerList[i][2] == 0.0: # exclude useless players and return immediately
            continue
        if playerList[i][4] == "GK":
            GKList.append(playerList[i])
        elif playerList[i][4] == "DEF":
            DEFList.append(playerList[i])
        elif playerList[i][4] == "MID":
            MIDList.append(playerList[i])
        else:
            FORList.append(playerList[i])

    # sort the 4 position lists and then get rid of any player who is outside the top 8
    GKList = sortList(GKList)
    DEFList = sortList(DEFList)
    MIDList = sortList(MIDList)
    FORList = sortList(FORList)

    # start a timer
    endTime = time.time() + 60 * minutes
    highest = 0
    counter = 0

    # while the time isnt up
    while time.time() < endTime:
        highest = bogoCreateTeam(GKList, DEFList, MIDList, FORList, highest)
        counter += 1

    # output the best team found after that time to the cmd, as well as a CSV file
    global bogoList
    d = pd.DataFrame(bogoList, columns=["Player", "Team", "Points", "Cost", "Position"])
    d.to_csv('team4.csv', index=False)
    print(bogoList)
    print("Highest points: %s" % highest)
    print("Total iterations: %s" % counter)
