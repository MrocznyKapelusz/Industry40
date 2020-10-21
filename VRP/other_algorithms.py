import csv

class DataStructure():
    
    def __init__(self, sourceFile:str):
        n = 0
        unit = ''
        with open('data/' + sourceFile, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            data = list(spamreader)
            # Save number of cities and units for later (might be useful)
            n=data[0][0]
            unit=data[1][0]
            # Delete 2 first rows
            data.pop(0)
            data.pop(0)

        self.n = int(n)     # number of cities (int)
        self.unit = unit    # unit (str)
        self.neighborhoodMatrix = []    # macierz sąsiedztwa

        # here it is a list of list of strings such as "118,031"
        for i in range(self.n): # 0..(n-1)
            self.neighborhoodMatrix.append(data[i])

        # here it is translated to a list of list of floats such as 118.031
        for row in range(self.n):
            self.neighborhoodMatrix[row][:] = map(lambda x: float(x.replace(',','.')), self.neighborhoodMatrix[row][:])

        # print(f"res: {list(res)}")
        # print(f"type(res): {type(res)}")
        





    def show(self):
        a = self.neighborhoodMatrix[24][23]
        print(f"showing : {a}")
        print(f"showing type : {type(a)}")

