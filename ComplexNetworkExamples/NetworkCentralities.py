#closeness
#degree centrality
#density
#betweeness centrality


matrix = [[0, [1, 2]], [1, [0, 2, 3]], [2, [0, 1, 3, 5]], [3, [1, 2, 4]], [4, [3, 5, 6]], [5, [4, 2]], [6, [4]]]
myPaths = []
myShortestPaths = []
myShortestPathsWithNodes = []
myCloseness=[]



def findpath(start, end, path=[]):
    path.append(start)
    if start == end:
        return path
    gg = [r for r in matrix[start][1] if r not in path]
    if gg == []:
        return path
    for vertex in gg:
        extended_paths = findpath(vertex, end, path)
        if extended_paths is None:
            return []
        if extended_paths != []:
            if extended_paths[-1] == end:
                return extended_paths
            else:
                return []


def findallpath(start, end, myPath=[]):
    #print("myPath {} for start {}, end {}".format(myPath, start, end))
    for t in range(0, len(matrix[start][1])):
        myPath.append([start])
        kk = matrix[start][1][t]
        c = findpath(kk, end, [])
        myPath[t].append(c)
    return myPath


# findallpath(0, 6)


#tüm path lari hesapla
def GetAllPaths():
    global myPaths
    visited = []
    for i in range(0, len(matrix)):
        visited.append(i)
        for j in range(1, len(matrix)):
            if matrix[j][0] in visited:
                continue
            c = findallpath(matrix[i][0], matrix[j][0], [])
            if c != []:
                myPaths.append(c)

#tüm kısa yolları hesapla
def CalculateShortestPaths():
    global myPaths,myShortestPaths,myShortestPathsWithNodes
    for i in range(0, len(myPaths)):
        tt = myPaths[i]

        for j in range(0, len(tt)):
            if len(tt[j][1])==0:
                continue
            t = [g for g in myShortestPaths if g[0]==tt[j][0] and g[1]==tt[j][1][-1]]
            count = len(tt[j][1])
            if t !=[]:
                if(count < t[0][-1]):
                    myShortestPaths[myShortestPaths.index(t[0])][-1]=count
                    
            else:
                myShortestPaths.append([tt[j][0],tt[j][1][-1],count])
                myShortestPathsWithNodes.append(tt[j])
    #print(myShortestPaths)
    #print("------------------------Tüm Pathler bitti------------------")




#ters yonlu shortest path ler ekleniyor
def CalculateAllShortestPaths():
    global myShortestPaths
    allNodes=[f[0] for f in matrix]
    tt=[]
    for i in allNodes:
        for j in allNodes:
            tt = [ g for g in myShortestPaths if g[0]==i and g[1]==j ]
            if tt==[]:
                tt = [ g for g in myShortestPaths if g[0]==j and g[1]==i ]            
                if tt!=[]:
                    myShortestPaths.append([tt[0][1],tt[0][0],tt[0][2]])
            tt=[]
    print(sorted(myShortestPaths))
    print("---------------------Tüm kısayollar bitti----------------------------")
    


#closeness hesaplama
# i node için n-1/(i inci nodun tüm node lara olan en kısa yollarının toplamı)

# myCloseness

def CalculateCloseness():
    global myShortestPaths
    allNodes=[f[0] for f in matrix]
    n = len(allNodes) - 1
    for i in allNodes:
        sn = sum([t[2] for t in myShortestPaths if t[0]==i])
        myCloseness.append([i, n/sn])
    dd=sorted(myCloseness, key=lambda t: t[1])
    print(dd)
    print("verilere göre closeness ı en yüksek olan node {}".format(dd[-1][0]))
    print("--------------------- Closeness lar biti--------------------")
        




GetAllPaths()
CalculateShortestPaths()
CalculateAllShortestPaths()
CalculateCloseness()

print("------------------------Node lara ait Degree ler (Degree Cenrality)---------------")
degreeNodes=[]

degreeNodes = [[g[0], len(g[1])] for g in matrix]
print(degreeNodes)


#betweeness centrality
for h in [f[0] for f in matrix]:
    for k in [f[0] for f in matrix]:
        if h!=k:
            #h ile k arasında geçen her bir node araştırılıyor
            for t in [f[0] for f in matrix]:
                #print(t)
                hh=[]
                #hh = [ff for ff in [[hh for hh in tt if hh[0]==0] for tt in myPaths] if ff!=[]]
                hh = [cc for cc in [[jj for jj in tt if jj[0]==h and t in jj[1] and h not in jj[1] and k not in jj[1]] for tt in myPaths]]
                #print("hh --------------- {}".format(hh))
                if hh!=[]:
                #    print("hh --------------- {}".format(hh))
                #    print("{} ile {} arasında {} var".format(h,k,t))
