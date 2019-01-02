# Random Network oluşturulması ve SIR modelinin simülasyonu
import math
import matplotlib.pyplot as plt
import numpy as np
import random as random

# sadece virtulization için yüklendi
import networkx as nx

# burayı en azından 200 tutmalısınız
nodeCount = 200
nodes = [[g, []] for g in range(0, nodeCount)]

stepCount = int(round((len(nodes) * (len(nodes) - 1)) / 2))

# eşik değer -3 ile 3 arasında olmalı
# rastgele üserilen rakam verilen rakamdan büyük ise iki nod arasında bağ kurulur
rn = 2


# oluşturulan rakamların random olmasını sağlamak için
# ve normal dağılıma sahip olabilmesi için
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
    r1 = random.randint(0, nodeCount - 1)
    r2 = random.randint(0, nodeCount - 1)
    # print(r1)
    cc = [g for g in nodes[r1]]

    if x[i] > rn:
        # print("eklendi")
        if cc[1] == []:
            nodes[r1][1].append(r2)
            nodes[r2][1].append(r1)
        else:
            dg = [d for d in cc[1] if d == r2]
            if dg == []:
                nodes[r1][1].append(r2)
                nodes[r2][1].append(r1)
                # else:
                # print("eklenmedi")
NodesItemsCount = [[f[0], len(f[1])] for f in nodes]

sorted(NodesItemsCount, key=lambda x: x[1])

distNumbers = []

distNumbers = [t[1] for t in NodesItemsCount if t[1] not in distNumbers and not distNumbers.append(t[1])]

sorted(distNumbers)
distCount = []

for j in distNumbers:
    distCount.append([j, len([g for g in NodesItemsCount if g[1] == j])])
print(distCount)

plt.scatter([t[0] for t in distCount], [t[1] for t in distCount])
plt.show()

G = nx.Graph()

for g in nodes:
    G.add_node(g[0])
    for t in g[1]:
        G.add_edge(g[0], t)

pos = nx.spring_layout(G)

nx.draw_networkx(G, pos)

plt.show()

# şu noktadan sonra SIR modelini simüle etmeye çalışıyoruz.




# her bir gün dönümünde

# 1. rasgele sayı üretiyoruz (0,1) verilen sayıdan büyük sayı çıkarsa
#       üzerinde olduğumuz node un hasta komşusu varsa o node u hasta olacak kabül ediyoruz.
# 2. rasgele sayı üretiyoruz (0,1) verilen sayıdan büyük sayı çıkarsa
#       üzerinde olduğumuz node hasta ise iyleşti kabül ediyoruz.


# seçilen node un hasta ise komşularını hasta etme olasılığı ya da
# kendi hasta değilse hasta komşularından hastalık alma olasılığı
InfectedRate = 0.5

# seçilen node hsta ise kendisinin iyleşme olasılığı
RecoveredRate = 0.46

# kaç gün için çalışacak
days = 30

# herbir node un hastalık bilgi durumu - SIR maodelini nezle için çalıştırıyoruz
# g = node index ve nodun title ı
# s = şimdilik tüm nodeların sağlıklı olduğunu düşünüyoruz
# False = 7 gün durumu sayılmaya başlamadan önce hastamıydı
# 0 = bu nodun kaç gündür  hastalıklı olduğunu söylüyor.
#     7 gün sonunda rastgele sağlıklı olma durumu olmazsa bile biz sağlıklı varsayacağız.


# durum kodları
i = "infected"
s = "susceptible"
r = "recovered"

nodesMeta = [[g, s, False, 0] for g in range(0, nodeCount)]

# !!!!!! not : bu çalışmada 7 günlük hesapla ilgili birşey
#             ileride yapılabilir bir fikir olsun diye yazıldı




# node lardan birisi rastgele seçilerek komşu nodeları da hasta olarak işaretleniyor

rint = random.randint(0, len(nodes) - 1)
nodesMeta[rint][1] = i
print("---------------------------------------------")

# ilgili nodun komşularını bul ve onları da hasta olarak işaretle
for h in [g for g in nodes if g[0] == rint]:
    nodesMeta[h[0]][1] = i


# node larda graph mış gibi dolaşmak gerekirse diye yazılan yardımcı fonksiyon
# şuan için kullanılmayacak bir fonksiyon
def getChildNodes(indx):
    childnodes = [g for f in nodes if nodes[0] == indx]
    for k in childnodes:
        # herbir childnode için yapılacak birşey varsa burada yapılabilir

        # childnode ların childnode ları için fonksiyonu çağır (recursive)
        getChildNodes(k)


illnessChange = []


infectedCount = len([f for f in nodesMeta if f[1] == i])
susceptibleCount = len([f for f in nodesMeta if f[1] == s])
recoveredCount = len([f for f in nodesMeta if f[1] == r])
illnessChange.append([infectedCount, susceptibleCount, recoveredCount, nodesMeta])

# verilen gün kadar işlem yapılır
for k in range(0, days):
    for g in nodes:
        # öncelikle kendisinin hasta olup olmadığına bakıyoruz.
        ff = [f for f in nodesMeta if f[0] == g[0]]

        # eğer hasta ise belli bir olasılıkla komşularını hasta edecek
        if ff[0][1] == i:
            # hasta nodun iyileşme ihtimali
            rnn = random.random()

            # eğer hasta node iyleşirse başka birine hastalık bulaştıramıyor
            if rnn > RecoveredRate:
                ff[0][1] = r
            else:
                # üzerinde çalıştığımız nodun hasta olmayan komşularını al
                # ve belli bir olasılıkla hasta olarak işaretle
                cc = [h for h in nodes if h[0] == ff[0][0]]
                if cc == []:
                    continue

                for j in cc[0][1]:
                    # j index li node asıl node un komşusu durumunda.
                    # eğer komşu node (j) un index i asıl node dun index inden daha küçükse,
                    # küçük indexe sahip olan bu node (j) kendisi asıl node iken zaten
                    # bu link üzerinden daha önce geçtiği için kodu devam ettirebiliriz
                    if j < g[0]:
                        continue

                    rr = [dd for dd in nodesMeta if dd[0] == j]
                    if rr != []:
                        if rr[0][1] != s:
                            rnn2 = random.random()
                            if rnn2 > InfectedRate:
                                rr[0][1] = i


        # hasta değilse komşularından hasta olan olup olmadığına bakıyoruz
        elif ff[0][1] == s:
            cc = [h for h in nodes if h[0] == ff[0][0]]
            if cc == []:
                continue

            for j in cc[0][1]:
                # j index li node asıl node un komşusu durumunda.
                # eğer komşu node (j) un index i asıl node dun index inden daha küçükse,
                # küçük indexe sahip olan bu node (j) kendisi asıl node iken zaten
                # bu link üzerinden daha önce geçtiği için kodu devam ettirebiliriz
                if j < g[0]:
                    continue

                rr = [dd for dd in nodesMeta if dd[0] == j]
                if rr[0][1] != i:
                    rnn3 = random.random()
                    if rnn3 > InfectedRate:
                        nodesMeta[nodesMeta.index(ff[0])][1] = i
                        # diğer node lara bakmamıza gerek yok
                        break
    infectedCount = len([f for f in nodesMeta if f[1] == i])
    susceptibleCount = len([f for f in nodesMeta if f[1] == s])
    recoveredCount = len([f for f in nodesMeta if f[1] == r])
    illnessChange.append([infectedCount, susceptibleCount, recoveredCount, nodesMeta])

# tüm işlem bittikten sonra grafikte göster
plt.plot([t[0] for t in illnessChange], "r")
plt.plot([t[1] for t in illnessChange], "g")
plt.plot([t[2] for t in illnessChange], "b")
plt.legend(['infected = red', 'susceptible = green', 'recovered = blue'], loc='upper right')


plt.show()
