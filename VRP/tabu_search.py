from other_algorithms import DataStructure, Vector
from goal_function import goalFunction
from sim_anneal import swap
from numpy import zeros

def tabu_search(data: DataStructure, hub:int, c:int, init_perm:Vector, limit:int, cadence: int) -> Vector:
    current_perm = init_perm
    result_perm = init_perm
    tabuList = zeros([data.n, data.n], int)   #   empty matrix

    for it in range(1,limit+1):
        c_best = goalFunction(data, current_perm)[0]
        for j in range(0,data.n):
            for k in range(j+1, data.n):
                if tabuList[j][k] < it:
                    new_perm = swap(current_perm, j, k)
                    res = goalFunction(data, new_perm)[0]
                    if res < c_best:
                        c_best = res
                        j_opt = j
                        k_opt = k
        current_perm = swap(current_perm, j_opt, k_opt)
        if goalFunction(data, current_perm)[0] < goalFunction(data, result_perm)[0]:
            result_perm = current_perm
        print(f"Iteration: {it}; Permutation: {result_perm}; Cost: {goalFunction(data, result_perm)[0]}.")
