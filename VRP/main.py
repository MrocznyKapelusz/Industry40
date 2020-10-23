import other_algorithms as oa
import permutation as perm
import goal_function as gf
import plot_on_map as plt

def main():
    n = 7  # number of cities
    h = 1   # hub's id
    c = 2   # number of cars

    # where to save the map
    mapFileName = "generatedMaps/map.html"

    # read data
    data = oa.DataStructure('PL.csv')

    permutation = perm.generatePermutation(data.n, h, c)
    print(f"Proponowana permutacja: {permutation}")
    result = gf.goalFunction(data, permutation)
    print(f"Koszt proponowanego rozwiązania: {result[0]} {result[1]}")
    plt.draw(data, permutation, mapFileName)

if __name__ == "__main__":
    main()
    # some comment