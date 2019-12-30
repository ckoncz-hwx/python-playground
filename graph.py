from sys import stdin, stdout

print("bemenet")
elso = [int (i) for i in stdin.readline().split()]
adat = []
for i in range(elso[1]):
    adat.append([int (i) for i in stdin.readline().split()])
print(adat)

def ciklus(n,m):
    for i in range(n):
        lista=[]
        for j in range(m):
            if (adat[j][0] == i+1):
                lista.append(adat[j])
 
def elagaz(n,m):
    for i in range(n):
        lista=[]
        for j in range(m):
            if (adat[j][0] == i+1):
                lista.append(adat[j])
        if (len(lista)>1):
            print(i+1)

ciklus(elso[0],elso[1])
