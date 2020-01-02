from sys import stdin, stdout
elso=[int (i) for i in stdin.readline().split()]
data=[]
adat=[]
for i in range(elso[1]):
    data.append([int (i) for i in stdin.readline().split()])
    adat.append([i for i in range(data[i][1],data[i][0]+1)])
szam=[0 for i in range(elso[0])]
for i in range(elso[1]):
    for j in range(len(adat[i])):
        szam[adat[i][j]-1]+=1
l=0
k=0
for i in range(elso[0]):
    if (szam[i]>l-1):
        l=szam[i]
        k=i+1
print(l,k)