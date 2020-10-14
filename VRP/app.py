from typing import List # to use type aliasing
import csv

# type alias
Vector = List[float]

# # This is an exapmle hot type aliasing works
# def scale(scalar: float, vector: Vector) -> Vector:
#     return [scalar * num for num in vector]
# new_vector = scale(2.0, [1.0, -4.2, 5.4])
# print(new_vector)


def generatePermutation(n:int) -> Vector:
    return [0, 2, 3, 1, 0]


def main():
    with open('data/PL.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        # for row in spamreader:
        #     print(', '.join(row))
        data = list(spamreader)
        print(str(data))


if __name__ == "__main__":
    # main()
    print(generatePermutation(5))