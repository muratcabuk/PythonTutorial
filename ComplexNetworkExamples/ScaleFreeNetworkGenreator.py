#Scale-Free - Real Network
import random as random
import matplotlib.pyplot as plt

matrix = [[0, [1, 2]], [1, [0, 2, 3]], [2, [0, 1]], [3, [1]]]
print("-----------------------------matrix ilk hali-----------------------")
print(matrix)

totalNode = 16
totalDegree = 0
totalGroupedegree = 0
indexRates = []
numbers = []
numbers2 = []
lasttt=[]


def GetDegrees():
    global totalDegree, indexRates, matrix
    totalDegree, indexRates = 0, []
    for i in range(0, len(matrix)):
        tt = len(matrix[i][1])
        mm = [x for x in indexRates if x[0] == tt]
        if mm:
            mm[0][1] += 1
        else:
            indexRates.append([tt, 1])
            totalDegree += tt


def GetRates():
    global totalGroupedegree, numbers, numbers2, indexRates
    totalGroupedegree, numbers, numbers2 = 0, [], []
    for j in range(0, len(indexRates)):
        totalGroupedegree += indexRates[j][0]
    for k in range(0, len(indexRates)):
        indexRates[k].append(indexRates[k][0] / totalGroupedegree)
    indexRates.sort(reverse=True)

    for g in range(0, len(indexRates)):
        c = round(indexRates[g][2] * 100)
        indexRates[g].append(c)
        numbers.append([indexRates[g][0] for x in range(c)])
        #print(numbers)
    numbers2 = [j for i in numbers for j in i]
    #random.shuffle(numbers2)
    #print("numbers len {}".format(len(numbers2)))


def CreateNodes():
    global totalNode, matrix, numbers, numbers2, lasttt
    GetDegrees()
    GetRates()
    for i in range(0, totalNode):
        rn = random.randint(1, len(matrix) - 1)
        for c in range(0, rn):
            rn2 = numbers2[random.randint(0, len(numbers2)-1)]
            #print(rn2)
            tt = [x for x in matrix if len(x[1]) == rn2]
            lasttt=tt            
            #print(tt)
            rn3 = 0
            if len(tt) != 1:
                rn3 = random.randint(0, len(tt) - 1)
            ss = tt[rn3][0]
            lm = len(matrix)
            matrix.append([lm, [ss]])
            matrix[ss][1].append(lm)
            GetDegrees()
            GetRates()

    #print(matrix)
    #print("-----------------------------matrix son hali-------------------------")
    plt.scatter([t[1:2] for t in indexRates],[t[0:1] for t in indexRates])
 
     
    #for i in range(len(indexRates)):
    #   plt.hlines(indexRates[i][2],0,indexRates[i][0]) # Here you are drawing the horizontal lines
    
    plt.show()


CreateNodes()
    
    
