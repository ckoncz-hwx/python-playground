from sys import stdin, stdout

elso = [int (i) for i in stdin.readline().split()]
x = int(stdin.readline())

ul=[0 for i in range(elso[0])]
rl=[0 for i in range(elso[0])]
rl[0]=elso[3]
for i in range(x):
    print(rl[0])
    print(sum(rl))
    for j in range(elso[0]):
        if (j+1 < elso[0]):
            ul[j+1]=rl[j]
            if (j+1>elso[1]-1 and j+1 <elso[1]+elso[2]):
                ul[0]+=rl[j]
    rl=ul
    ul=[0 for i in range(elso[0])]