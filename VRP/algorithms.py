from other_algorithms import DataStructure, Vector, Cars


def basicGreedyVRP_old(data: DataStructure, hub:int, c:int) -> Vector:
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
    # initialize empty final permutation
    perm = []
    # car's number
    # c = 1
    # maximum number of courses per car
    maxNumberOfCoursesPerCar = data.n/c

    # move hub to perm and remove from availableCities
    perm.append(availableCities.pop(availableCities.index(hub)))
    
    while(availableCities):
        # find currentFurthestCity from hub
        currentFurthestCity = -1
        currentFurthestDistance = float('-inf')
        for city in availableCities:
            distanceFromCurrentCity = data.neighborhoodMatrix[hub][city]
            if(distanceFromCurrentCity > currentFurthestDistance):
                currentFurthestDistance = distanceFromCurrentCity
                currentFurthestCity = city
            else:
                pass
        # now I have the furthest available city from hub

        # move that current furthest city to perm right after hub
        perm.append(availableCities.pop(availableCities.index(currentFurthestCity)))

        currentCarNumberOfCourses = 1

        print("Resetting limit to true")
        limit = True
        while limit:
            if currentCarNumberOfCourses < maxNumberOfCoursesPerCar and availableCities:
                latestCity = currentFurthestCity
                # find closest city from availableCities to the latestCity
                currentNearestCity = -1
                currentNearestDistanceFromLatestCity = float('inf')
                for city in availableCities:
                    distanceFromLatestCity = data.neighborhoodMatrix[latestCity][city]
                    if(distanceFromLatestCity < currentNearestDistanceFromLatestCity):
                        currentNearestDistanceFromLatestCity = distanceFromLatestCity
                        currentNearestCity = city
                    else:
                        pass
                # now I have the nearest city from latestCity

                # now add that city to the perm while popping from available
                perm.append(availableCities.pop(availableCities.index(currentNearestCity)))
                # update latestCity
                latestCity = currentNearestCity
                # increment # of courses
                currentCarNumberOfCourses += 1
                # repeat till limit is not reached
            else:
                # return to hub
                perm.append(hub)
                # when limit has been reached
                limit = False

    return perm




def advancedGreedyVRP(data: DataStructure, hub:int, c:Cars) -> Vector:
    """This is an advanced greedy Vehicle Route Problem algorithm.
    It starts with furthest city from the hub and comes back by choosing locally closest city to the chosen previously,
    and checking if the cargo fits in the car. If the cargo does not fit, the car is not full.
    Args:
        data (DataStructure):   read data
        hub (int):              hub's id
        c (Cars):               List of cars
    Returns:
        perm (Vector): Generated permutation as a List[int]
    """
    # create list of available cities
    availableCities = list(map(lambda x: x.id, data.cities))
    # initialize empty final permutation
    perm = []
    # car's number
    currentCar = 1
    # maximum number of courses per car
    # maxNumberOfCoursesPerCar = data.n/c



    # move hub to perm and remove from availableCities
    perm.append(availableCities.pop(availableCities.index(hub)))
    
    while(availableCities):
        # find currentFurthestCity from hub
        currentFurthestCity = -1
        currentFurthestDistance = float('-inf')
        for city in availableCities:
            distanceFromCurrentCity = data.neighborhoodMatrix[hub][city]
            if(distanceFromCurrentCity > currentFurthestDistance):
                currentFurthestDistance = distanceFromCurrentCity
                currentFurthestCity = city
            else:
                pass
        # now I have the furthest available city from hub

        # move that current furthest city to perm right after hub
        perm.append(availableCities.pop(availableCities.index(currentFurthestCity)))

        # add cargo from current furthest city to car
        currentCarCargoWeight = data.tasks[currentFurthestCity].weight
        currentCarCargoSize = data.tasks[currentFurthestCity].size


        # print("Resetting limit to true")
        limit = True
        while limit:
            # if the car can go and there is a city to go to
            if  currentCarCargoWeight<c.cars[currentCar].capacity and currentCarCargoSize<c.cars[currentCar].size and availableCities:
                latestCity = currentFurthestCity
                # find closest city from availableCities to the latestCity
                currentNearestCity = -1
                currentNearestDistanceFromLatestCity = float('inf')
                for city in availableCities:
                    distanceFromLatestCity = data.neighborhoodMatrix[latestCity][city]
                    if(distanceFromLatestCity < currentNearestDistanceFromLatestCity):
                        currentNearestDistanceFromLatestCity = distanceFromLatestCity
                        currentNearestCity = city
                    else:
                        pass
                # now I have the nearest city from latestCity
                

                if (currentCarCargoWeight+data.tasks[currentNearestCity].weight < c.cars[currentCar].capacity and \
                currentCarCargoSize+data.tasks[currentNearestCity].size < c.cars[currentCar].size):

                    # now add that city to the perm while popping from available
                    perm.append(availableCities.pop(availableCities.index(currentNearestCity)))
                    # update latestCity
                    latestCity = currentNearestCity
                    # increment # of courses
                    currentCarCargoWeight += data.tasks[latestCity].weight
                    currentCarCargoSize += data.tasks[latestCity].size
                    # repeat till limit is not reached
                else:
                    # return to hub
                    perm.append(hub)
                    # when limit has been reached
                    limit = False
            else:
                # return to hub
                perm.append(hub)
                # when limit has been reached
                limit = False

    return perm