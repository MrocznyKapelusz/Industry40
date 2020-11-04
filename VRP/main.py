import other_algorithms as oa
import permutation as perm
import goal_function as gf
import plot_on_map as plt
import algorithms as alg
import sim_anneal as sa
import matplotlib.pyplot as plt

def main():
    hub = 1   # hub's id
    c = 10   # number of cars
    cars = oa.Cars(2,5) # configure the car fleet

    # where to save the map
    mapFileName = "generatedMaps/map.html"

    # read data
    citiesSourceName = 'PL.csv'
    tasksSourceName = 'PLdata.csv'
    data = oa.DataStructure(citiesSourceName,tasksSourceName)

    """LAB1"""
    # permutation = perm.generatePermutation(data.n, hub, c)
    # print(f"Proponowana permutacja: {permutation}")
    # result = gf.goalFunction(data, permutation)
    # print(f"Koszt proponowanego rozwiązania: {result[0]} {result[1]}")
    # plt.draw(data, permutation, mapFileName)

    """LAB2"""
    # results=[]
    # for hub in range(0,25):
    #     # basicGreedyPermutation = alg.greedyVRP(data, hub, c)
    #     # print(f"Final Permutation for hub {hub}: {basicGreedyPermutation}")

    #     advancedGreedyPermutation = alg.greedyCVRP(data,hub,cars)
    #     print(f"Final Permutation for hub {data.cities[hub]}: {advancedGreedyPermutation}")

    #     # plt.draw(data, basicGreedyPermutation, mapFileName, sourceName)
    #     result = gf.goalFunction(data, advancedGreedyPermutation)
    #     results.append(result)
    #     print(f"Koszt proponowanego rozwiązania dla hub:{data.cities[hub]} : {result[0]} {result[1]}")

    # print(f"Optymalne położenie hub: {data.cities[results.index(min(results))]}, rozwiąwiązanie wynosi wtedy: {min(results)[0]} {min(results)[1]}")
    
    """LAB3"""
    basicGreedyPermutation = alg.greedyVRP(data, hub, c)
    print(f"Basic perm: {basicGreedyPermutation} of cost: {gf.goalFunction(data, basicGreedyPermutation)}")

    # ranodmPermutation=perm.generatePermutation(data.n,hub,c)
    # print(f"Random perm: {ranodmPermutation} of cost: {gf.goalFunction(data, ranodmPermutation)}")
    
    results=[]
    simAnnealPermutation=sa.sim_anneal(data,basicGreedyPermutation,25,1000,results)
    print(f"SimAnneal perm: {simAnnealPermutation} of cost: {gf.goalFunction(data, simAnnealPermutation)}")

    # print(len(results))
    # print(min(results))
    # print(results[-1])
    plt.plot(range(len(results)),results)
    plt.show()


if __name__ == "__main__":
    main()
    # some comment