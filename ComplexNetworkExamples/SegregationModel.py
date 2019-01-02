#segregation model test
from random import randint
import matplotlib.pyplot as plt
import copy as copy
import numpy as np

fig, ax = plt.subplots()



def drawplot(mymatrix):
    # gridi bas
    plt.pause(0.05)
    mydata = np.array(mymatrix)

    # data yı giride bas
    #for (iiii, jjjj), z in np.ndenumerate(mydata):
    #    ax.text(jjjj, iiii, z)

    ax.imshow(mydata, vmin=0.0, vmax=1.0)



w, h = 15, 15
count = 2

matrix = [[randint(0, 1) for x in range(w)] for y in range(h)]

matrixold=copy.deepcopy(matrix)

#aktif plotun ayarları
plt.ion()
ax.set_xticks(np.arange(0, w-1, 1))
ax.set_yticks(np.arange(0, h-1, 1))
plt.grid()





print(len(matrix))
print(len(matrix[0]))

print(matrix)

drawplot(matrix)



for cc in range(0,count):
    

    for i in range(0, w-1):
        for j in range(0, h-1):
    
            m = matrix[i][j]
        
            # şunanki node un durumu
        
            # eğer ilk satırdaysak geri geleme durumu kontrol eilmeli ancak ileri gitmede problem yok
            # eğer son satırdaysak ileri gitme durumu kontrol edişlmeli geri gitmede problem yok
            if i == 0:
                i1 = w - 1
                i2 = i + 1
            elif i == w - 1:
                i1 = i - 1
                i2 = 0
            else:
                i1 = i - 1
                i2 = i + 1
        
            # eğer ilk sütundaysak geri geleme durumu kontrol eilmeli ancak ileri gitmede problem yok
            # eğer son sütundaysak ileri gitme durumu kontrol edilmeli ancak geri gitmede problem yok
            if j == 0:
                j1 = h - 1
                j2 = j + 1
            elif j == h - 1:
                j1 = j - 1
                j2 = 0
            else:
                j1 = j - 1
                j2 = j + 1
        
            # 0 ve 1 lerin sayısı
            t0, t1, tt = 0, 0, 0
        
            if m == 0:
                t0 = t0 + 1
            elif m == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i1][j1] == 0:
                t0 = t0 + 1
            elif matrix[i1][j1] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i1][j] == 0:
                t0 = t0 + 1
            elif matrix[i1][j] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i1][j2] == 0:
                t0 = t0 + 1
            elif matrix[i1][j2] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i][j1] == 0:
                t0 = t0 + 1
            elif matrix[i][j1] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i][j2] == 0:
                t0 = t0 + 1
            elif matrix[i][j2] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i2][j1] == 0:
                t0 = t0 + 1
            elif matrix[i2][j1] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i2][j] == 0:
                t0 = t0 + 1
            elif matrix[i2][j] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            if matrix[i2][j2] == 0:
                t0 = t0 + 1
            elif matrix[i2][j2] == 1:
                t1 = t1 + 1
            else:
                tt = tt + 1
        
            # region Description
            # print("node un değeri {}".format(m))
            # print("1 sayısı: {}".format(t1))
            # print("0 sayısı: {}".format(t0))
            # print("boşluk sayısı: {}".format(tt))
            # endregion
        
        
            if m == 0 and t0 > t1 or m == 1 and t1 > t0:
                # print("taşımaya gerek yok")
                continue
        
            # print("--------------------")
        
            # print("taşınacak node {} - {} değeri {}".format(i, j, m))
        
            # yeni gidilecek yerin durumu. burada -1 yeni node alabilir demek
            # burası sadece -1 olanlardan gelmeli
            mr, ri, rj = 0, 0, 0
            f = True
            for iii in range(0, w - 1):
                if f==False:
                    break
                for jjj in range(0, h - 1):
        
                    ri = iii
                    rj = jjj
                    mr = matrix[ri][rj]
                    if mr == m:
                        continue
        
                    # print("seçilen node {} - {} değeri {}".format(ri, rj, mr))
        
                    # eğer ilk satırdaysak geri geleme durumu kontrol eilmeli ancak ileri gitmede problem yok
                    # eğer son satırdaysak ileri gitme durumu kontrol edişlmeli geri gitmede problem yok
                    if ri == 0:
                        ri1 = w - 1
                        ri2 = ri + 1
                    elif ri == w - 1:
                        ri1 = ri - 1
                        ri2 = 0
                    else:
                        ri1 = ri - 1
                        ri2 = ri + 1
        
                    # eğer ilk sütundaysak geri geleme durumu kontrol eilmeli ancak ileri gitmede problem yok
                    # eğer son sütundaysak ileri gitme durumu kontrol edilmeli ancak geri gitmede problem yok
                    if rj == 0:
                        rj1 = h - 1
                        rj2 = rj + 1
                    elif rj == h - 1:
                        rj1 = j - 1
                        rj2 = 0
                    else:
                        rj1 = rj - 1
                        rj2 = rj + 1
        
                    # 0 ve 1 lerin sayısı
                    s0, s1, ss = 0, 0, 0
        
                    if mr == 0:
                        s0 = s0 + 1
                    elif mr == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri1][rj1] == 0:
                        s0 = s0 + 1
                    elif matrix[ri1][rj1] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri1][rj] == 0:
                        s0 = s0 + 1
                    elif matrix[ri1][rj] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri1][rj2] == 0:
                        s0 = s0 + 1
                    elif matrix[ri1][rj2] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri][rj1] == 0:
                        s0 = s0 + 1
                    elif matrix[ri][rj1] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri][rj2] == 0:
                        s0 = s0 + 1
                    elif matrix[ri][rj2] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri2][rj1] == 0:
                        s0 = s0 + 1
                    elif matrix[ri2][rj1] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri2][rj] == 0:
                        s0 = s0 + 1
                    elif matrix[ri2][rj] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        
                    if matrix[ri2][rj2] == 0:
                        s0 = s0 + 1
                    elif matrix[ri2][rj2] == 1:
                        s1 = s1 + 1
                    else:
                        ss = ss + 1
        

                    if mr == 0 and s0 > s1 or mr == 1 and s1 > s0:
                        continue
                    else:
                        matrix[i][j] = mr
                        matrix[ri][rj] = m
                        f=False
                        # print("taşındı")
                        #print(matrix)
                        drawplot(matrix)




fig1, ax1 = plt.subplots()                   
ax1.set_xticks(np.arange(0, w-1, 1))
ax1.set_yticks(np.arange(0, h-1, 1))
plt.grid()
mydata = np.array(matrixold)
ax1.imshow(mydata, vmin=0.0, vmax=1.0)
plt.plot()


