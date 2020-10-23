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
            # now I have furthest city from hub

    # move that furthest city to perm right after hub
    perm.append(availableCities.pop(availableCities.index(furthestCity)))

    print(f"perm: {perm}")
    print(f"avCit: {availableCities}")

    # # lets sey Ive got only 1 car rn
    # while(availableCities):

    return perm