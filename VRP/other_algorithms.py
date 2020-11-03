import csv
from typing import List # to use type aliasing
import pathlib
import os
BASEDIR=os.path.dirname(__file__)
# print(os.path.dirname(__file__))

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


class CargoTask():
    def __init__(self,city,length,weight):
        self.city=city
        self.size=length
        self.weight=weight
    def __repr__(self):
        return repr('CargoTask no. '+str(self.city)+' '+str(self.size)+' '+str(self.weight))

class DataStructure():    

    def __init__(self,sourceFileCities,sourceFileTasks=None):
        n = 0
        unit = ''
        
        with open(str(BASEDIR)+'/data/' + sourceFileCities, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            dataCities = list(spamreader)
            # Save number of cities and units for later (might be useful)
            n=dataCities[0][0]
            unit=dataCities[1][0]
            # Delete 2 first rows
            dataCities.pop(0)
            dataCities.pop(0)

        

        self.n = int(n)     # number of cities (int)
        self.unit = unit    # unit (str)
        self.neighborhoodMatrix = []    # macierz sąsiedztwa
        self.cities = []    # list of City objects
        

        # here it is a list of list of strings such as "118,031"
        for i in range(self.n): # 0..(n-1)
            self.neighborhoodMatrix.append(dataCities[i])

        # here it is translated to a list of list of floats such as 118.031
        for row in range(self.n):
            self.neighborhoodMatrix[row][:] = map(lambda x: float(x.replace(',','.')), self.neighborhoodMatrix[row][:])

        # read all cities
        for c in range (self.n,2*self.n):
            # print(f"[0]: " + dataCities[c][0] + " [1]: " + dataCities[c][1] + " [2]: " + dataCities[c][2] + " [3]: " + dataCities[c][3])
            city = City(dataCities[c][0], dataCities[c][1], float(dataCities[c][2].replace(',','.')), float(dataCities[c][3].replace(',','.')), c-self.n)
            self.cities.append(city)


        if(sourceFileTasks is not None):
            self.tasks=[]      # list of CargoTask objects

            with open(str(BASEDIR)+'/data/' + sourceFileTasks, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
                dataTasks = list(spamreader)
                num_of_tasks=dataTasks[0][0]
                dataTasks.pop(0)
            
            # read all tasks
            for task in range(len(dataTasks)):
                cargoTask=CargoTask(int(dataTasks[task][0])-1,float(dataTasks[task][1].replace(',','.')),float(dataTasks[task][2]))
                self.tasks.append(cargoTask)

        # for city in self.cities:
        #     print(city)

        # for task in self.tasks:
        #     print(task)

class Car():
    def __init__(self, size):
        # BIG car
        if(size=='b'): 
            self.size=16.6
            self.capacity=24000
        # SMALL car
        elif(size=='s'):
            self.size=7.8
            self.capacity=8000

class Cars():
    """
    This class creates and holds a list of all available cars.
    """
    cars=[]
    def __init__(self, b:int,s:int):
        self.size=b+s
        for car in range(b):
            self.cars.append(Car('b'))
        for car in range(s):
            self.cars.append(Car('s'))