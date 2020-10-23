import csv
from typing import List # to use type aliasing

# type alias
Vector = List[int]

class City():
    def __init__(self, postalCode, name, latitude, longitude, id):
        self.postalCode = postalCode
        self.name = name
        self.latitude = latitude    # najpierw jest latitude = szerokość
        self.longitude = longitude  # druga jest longitude = długość
        self.id = id

    def __repr__(self):
        # return repr('City ' + self.name)
        return repr('City no. ' + str(self.id) + ' ' + self.name)


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
        self.cities = []    # list of City objects

        # here it is a list of list of strings such as "118,031"
        for i in range(self.n): # 0..(n-1)
            self.neighborhoodMatrix.append(data[i])

        # here it is translated to a list of list of floats such as 118.031
        for row in range(self.n):
            self.neighborhoodMatrix[row][:] = map(lambda x: float(x.replace(',','.')), self.neighborhoodMatrix[row][:])

        # read all cities
        for c in range (self.n,2*self.n):
            # print(f"[0]: " + data[c][0] + " [1]: " + data[c][1] + " [2]: " + data[c][2] + " [3]: " + data[c][3])
            city = City(data[c][0], data[c][1], float(data[c][2].replace(',','.')), float(data[c][3].replace(',','.')), c-self.n)
            self.cities.append(city)

        for city in self.cities:
            print(city)