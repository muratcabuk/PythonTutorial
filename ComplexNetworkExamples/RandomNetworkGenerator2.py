#Random Network

import numpy as np
import math
import matplotlib.pyplot as plt
import random as random

#sadece virtulization için yüklendi
import networkx as nx
import matplotlib.pyplot as plt





nodeCount = 200
nodes = [[g,[]] for g in range(0, nodeCount)]
stepCount = int(round((len(nodes) * (len(nodes) - 1)) / 2))

#eşik değer -3 ile 3 arasında olmalı
#rastgele üserilen rakam verilen rakamdan büyük ise iki nod arasında bağ kurulur
rn = 2






#oluşturulan rakamların random olmasını sağlamak için
#ve normal dağılıma sahip olabilmesi için
#tabi bu konu için burası zorunlu değil sadece normal dağılımlısayı üretmek için test için yazıldı
def get_gaussian_random():
    m = 0
    while m == 0:
        m = round(np.random.random() * 100)

    numbers = np.random.random(int(m))
    summation = float(np.sum(numbers))
    gaussian = (summation - m / 2) / math.sqrt(m / 12.0)

    return round(gaussian, 1)


x = []

for i in range(0, stepCount):
    x.append(get_gaussian_random())

xcount = []

for i in range(0, len(x)):
    gg = [f for f in xcount if f[0] == x[i]]

    if (gg != []):
        xcount[xcount.index(gg[0])][1] += 1
    else:
        xcount.append([x[i], 1])

plt.scatter([t[0] for t in xcount], [t[1] for t in xcount])
plt.show()



for i in range(stepCount):
    r1 = random.randint(0, nodeCount-1)
    r2 = random.randint(0, nodeCount-1)
    #print(r1)
    cc = [g for g in nodes[r1]]

    if x[i] > rn:
        #print("eklendi")
        if cc[1] ==[]:
            nodes[r1][1].append(r2)
            nodes[r2][1].append(r1)
        else:
            dg = [d for d in cc[1] if d == r2]
            if dg  == []:
                nodes[r1][1].append(r2)
                nodes[r2][1].append(r1)
    #else:
        #print("eklenmedi")
NodesItemsCount = [[f[0],len(f[1])] for f in nodes]

sorted(NodesItemsCount,key = lambda x : x[1])

distNumbers=[]

distNumbers = [t[1] for t in NodesItemsCount if t[1] not in distNumbers and not distNumbers.append(t[1])]

sorted(distNumbers)
distCount=[]

for j in  distNumbers:
    distCount.append([j, len([g for g in NodesItemsCount if g[1] == j])])
print(distCount)    


plt.scatter([t[0] for t in distCount], [t[1] for t in distCount])
plt.show()

G = nx.Graph()

for g in nodes:
    G.add_node(g[0])
    for t in g[1]:
        G.add_edge(g[0],t)

pos = nx.spring_layout(G)

nx.draw_networkx(G,pos)

plt.show()













