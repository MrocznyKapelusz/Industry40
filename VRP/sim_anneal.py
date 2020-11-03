from other_algorithms import DataStructure, Vector, Cars
from goal_function import goalFunction
from math import sqrt,exp,log
import random
from copy import copy
startTemp=[100,1000,10000]
alfa=[0.97,0.95,0.90]



def sim_anneal(data:DataStructure,permutation:Vector,endTemp:int,startTemp:int,results:Vector)->Vector:
    N=len(permutation)
    
    # epochs=int(sqrt(N))
    # epochs=N
    epochs=N**2

    currentTemp=startTemp
    current_perm=copy(permutation)
    it=1

    # results=[]
    while currentTemp > endTemp:
        # print(f"Current T = {currentTemp}")
        for k in range(epochs):
            i=random.randint(0,N-1)
            j=random.randint(0,N-1)

            new_perm=adjacentSwap(current_perm,i)
            # new_perm=swap(current_perm,i,j)
            # new_perm=insert(current_perm,i,j)

            deltaCmax=goalFunction(data,current_perm)[0]-goalFunction(data,new_perm)[0]
            if(deltaCmax<0): # new solution is worse
                r=random.random()
                if(r>=exp(deltaCmax/currentTemp)):
                    current_perm=copy(new_perm)
            else: #new solution is better
                current_perm=copy(new_perm)
            results.append(goalFunction(data,current_perm)[0])
        
        # currentTemp=currentTemp*0.99
        currentTemp=currentTemp-(startTemp/(startTemp*0.1))
        # currentTemp=currentTemp/log(it+1)
        it+=1
    # return results
    return current_perm     


# swap positions of two elements in a permutation
def swap(permutation:Vector,pos1:int,pos2:int)->Vector:
    tmpList=copy(permutation)
    tmpList[pos1],tmpList[pos2]=tmpList[pos2],tmpList[pos1]
    return tmpList

# pos1 - element; pos2- position to instert
def insert(permutation:Vector,pos1:int, pos2:int)->Vector:
    tmpList=copy(permutation)
    if pos2==len(permutation):
        tmp=tmpList.pop(pos1)
        tmpList.append(tmp)
    else:
        tmp=tmpList.pop(pos1)
        tmpList.insert(pos2,tmp)
    return tmpList

def adjacentSwap(permutation:Vector,pos1:int):
    if(pos1!=len(permutation)-1):
        return swap(permutation,pos1,pos1+1)
    else:
        return swap(permutation,pos1,pos1-1)

if __name__=='__main__':
    test=[1,2,3,4]
    foo=insert(test,1,3)
    print(test)
    print(foo)