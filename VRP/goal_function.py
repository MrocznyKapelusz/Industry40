import permutation as perm
from typing import List # to use type aliasing
from other_algorithms import DataStructure

# type alias
Vector = List[int]

# TODO: save the list of cities to a new list?

def goalFunction(data: DataStructure, permutation:Vector)->int:
    """
    This function takes in a string and a Vector. The string is the name of the file
    that contains data about the cities and their distances. The Vector is a permutation 
    that is a proposed solution of the VRP problem.

    The function returns a tuple of the cost of the solution (distance) and the unit in which it is calculated (str).
    """
    cost = 0

    # Sum up the cost of all the distances, parse to float 
    for city in range(len(permutation)-1):
        cost += data.neighborhoodMatrix[permutation[city]][permutation[city+1]]

    return (cost,data.unit)


def main():
    n = 7  # number of cities
    h = 0   # hub's id 
    c = 2   # number of cars

    permutation = perm.generatePermutation(n, h, c)
    print(f"Proponowana permutacja: {permutation}")
    result=goalFunction('PL.csv',permutation)
    print(f"Koszt proponowanego rozwiązania: {result[0]} {result[1]}")

if __name__ == "__main__":
    main()