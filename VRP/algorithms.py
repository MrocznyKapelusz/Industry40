from other_algorithms import DataStructure, Vector


def basicGreedyVRP(data: DataStructure, hub:int, c:int) -> Vector:
    """This is basic greedy Vehicle Route Problem algorithm.
    It starts with furthest city from the hub and comes back by choosing locally closest city to the chosen previously.
    Args:
        data (DataStructure):   read data
        hub (int):              hub's id
        c (int):                number of cars
    Returns:
        perm (Vector): Generated permutation as a List[int]
    """



    # create list of available cities
    availableCities = list(map(lambda x: x.id, data.cities))

    print(f"from 18(Bydgoszcz) to 12(Koszalin): " + str(data.neighborhoodMatrix[18][12]))
    print(f"from 18(Bydgoszcz) to 21(Kutno): " + str(data.neighborhoodMatrix[18][21]))



    # initialize empty permutation
    perm = []
    # car's number
    c = 1

    # move hub to perm and remove from availableCities
    perm.append(availableCities.pop(availableCities.index(hub)))
    
    # find furthest city from hub from all availableCities
    furthestCity = -1
    maxDistanceFromHub = float('-inf')
    for city in availableCities:
        distanceFromHub = data.neighborhoodMatrix[hub][city]
        if(distanceFromHub > maxDistanceFromHub):
            maxDistanceFromHub = distanceFromHub
            furthestCity = city
        else:
            pass
        # now I have furthest city from hub

    # move that furthest city to perm right after hub
    perm.append(availableCities.pop(availableCities.index(furthestCity)))

    print(f"perm: {perm}")
    print(f"avCit: {availableCities}")

    # lets sey Ive got only 1 car rn
    latestCity = furthestCity
    while(availableCities):
        # find clostest city from availableCities to the latestCity
        curNearestCity = -1
        minDistanceFromLatestCity = float('inf')
        for city in availableCities:
            distanceFromLatestCity = data.neighborhoodMatrix[latestCity][city]
            if(distanceFromLatestCity < minDistanceFromLatestCity):
                minDistanceFromLatestCity = distanceFromLatestCity
                curNearestCity = city
            else:
                pass
        # now I have the nearest city from latestCity

        # now add that city to the perm while popping from available
        perm.append(availableCities.pop(availableCities.index(curNearestCity)))
        # update latestCity
        latestCity = curNearestCity
        # repeat till there are no more availableCities


    # return to hub at the end
    perm.append(hub)

    return perm