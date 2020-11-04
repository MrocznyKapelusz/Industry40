import other_algorithms as oa
import permutation as perm
import goal_function as gf
import plot_on_map as plt
import algorithms as alg
import sim_anneal as sa
import matplotlib.pyplot as plt
import tabu_search as ts


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


    # # VRP() (greedy)
    # # cVRP() (greedy w/ cargo limit)
    # """LAB2"""
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


    # simulated annealing
    # tabu search
    """LAB3"""
    init_perm = perm.generatePermutation(data.n, hub, c, True)
    initRes = gf.goalFunction(data, init_perm)
    print(f"Initial permutation: {init_perm}.\nCost: {initRes[0]} {initRes[1]}.")
    print('-'*25)
    ts.tabu_search(data, hub, c, init_perm = init_perm, limit=100, cadence=7)

    # basicGreedyPermutation = alg.greedyVRP(data, hub, c)
    # print(f"Basic perm: {basicGreedyPermutation} of cost: {gf.goalFunction(data, basicGreedyPermutation)}")
    # results=[]
    # simAnnealPermutation=sa.sim_anneal(data,basicGreedyPermutation,100,10000,results)
    # print(f"SimAnneal perm: {simAnnealPermutation} of cost: {gf.goalFunction(data, simAnnealPermutation)}")
    # print(len(results))
    # print(results[-1])
    # plt.plot(range(len(simAnnealPermutation)),simAnnealPermutation)
    # plt.show()



if __name__ == "__main__":
    main()
    # some comment