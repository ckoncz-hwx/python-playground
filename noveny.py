from sys import stdin, stdout

elso = [int (i) for i in stdin.readline().split()]
x = int(stdin.readline())

ul=[]
rl=[1 for i in range(elso[3])]
for i in range(x):
    print(rl.count(1))
    print(len(rl))
    for j in range(len(rl)):
        if (rl[j] < elso[0]):
            ul.append(rl[j]+1)
            if (rl[j]>elso[1]-1 and rl[j]<elso[1]+elso[2]):
                ul.append(1)
    rl=ul
    ul=[]