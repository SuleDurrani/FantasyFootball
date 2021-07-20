import time

from BogoSolver import bogoTeamFinder
from EqualPriceSolver import findHighestPointsWithinEqualCost
from AverageSolver import findBestAverage
from OptimalPCRatioSolver import optimalPlayers


def main():
    # Budget = 83.8
    # 7.618m per player
    # best team irrespective of cost is 1691
    # best ive found cost inclusive is 1583
    # (71*1)+(211*210*209*208)+(261*260*259*258)+(121*120) different combos with original dataset
    # 6,460,799,831 total.
    # 3424 combinations with 8 players each position ((8*1)+(8*7*6*5)+(8*7*6*5)+(8*7)) with my trimming

    start_time = time.time()
    optimalPlayers()
    print("--- " + str(time.time() - start_time) + " seconds ---\n")

    start_time = time.time()
    findBestAverage()
    print("--- " + str(time.time() - start_time) + " seconds ---\n")

    start_time = time.time()
    findHighestPointsWithinEqualCost()
    print("--- " + str(time.time() - start_time) + " seconds ---\n")

    bogoTeamFinder(1)


if __name__ == "__main__":
    main()
