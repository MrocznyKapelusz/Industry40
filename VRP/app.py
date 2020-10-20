from typing import List # to use type aliasing
import csv
from random import randint
from collections import Counter # to count distinct objects in a list
import time

# type alias
Vector = List[int]

# # This is an exapmle hot type aliasing works
# def scale(scalar: float, vector: Vector) -> Vector:
#     return [scalar * num for num in vector]
# new_vector = scale(2.0, [1.0, -4.2, 5.4])
# print(new_vector)


def generatePermutation(n:int, h:int, c:int) -> Vector:
    """This function generates random permutation for given starting (and ending) city (aka HUB)

    Right now it visits every city once and uses from 1 to maximum cars.
    Some cars may have "empty" rides

    Args:
        n (int): Number of cities
        h (int): Index of starting city (hub)
        c (int): Number of cars

    Returns:
        perm (Vector): Generated permutation as a List[int]

    Example:
        If there are 5 cities, then indexes are 0...4.
        generatePermutation(5, 0, 1) will produce e.g. such output:
        [0, 3, 4, 1, 0]
    """
    ############################
    # config params
    # everyCarIsUsed = True
    everyCityIsVisited = True
    #############################

    # counts distinct objects in a list
    def countDistinct(arr): 
        return len(Counter(arr).keys())

    # create list only w/ hub at the beginning
    perm = [h]
    # print (perm)
    # time.sleep(3)
    visitedCities = [h]
    noOfUsedCars = 1

    #now use every car (HARDCODED)
    if everyCityIsVisited:
        while countDistinct(visitedCities) < n:
            randNum = randint(0, n-1)
            # print(f"Current rand: {randNum}, Current list: {perm}")
            
            # is the city a hub?
            if randNum == h:
                if noOfUsedCars == c:
                    continue
                else:
                    perm.append(randNum)
                    noOfUsedCars+=1
                    continue
            # selected city is not a hub
            else:
                # city not yet visited
                if randNum not in visitedCities:
                    perm.append(randNum)
                    visitedCities.append(randNum)
                # city already visited
                else:
                    continue
        perm.append(h)
    return perm



def main():
    with open('data/PL.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        # for row in spamreader:
        #     print(', '.join(row))
        data = list(spamreader)
        print(str(data))
    n = 97  # number of cities
    h = 7   # hub's id 
    c = 4   # number of cars

    permutation = generatePermutation(n, h, c)
    print(permutation)


if __name__ == "__main__":
    main()