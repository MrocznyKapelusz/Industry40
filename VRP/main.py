import permutation as perm
import goal_function as gf

def main():
    n = 7  # number of cities
    h = 0   # hub's id 
    c = 2   # number of cars

    permutation = perm.generatePermutation(n, h, c)
    print(f"Proponowana permutacja: {permutation}")
    result = gf.goalFunction('PL.csv',permutation)
    print(f"Koszt proponowanego rozwiązania: {result[0]} {result[1]}")

if __name__ == "__main__":
    main()