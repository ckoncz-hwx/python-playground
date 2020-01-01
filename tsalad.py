from sys import stdin, stdout

n = int(stdin.readline())
data = []
apa = set()
for i in range(n-1):
   m = int(stdin.readline())
   data.append(m)
   apa.add(m)
lista ={i+1 for i in range(10)}
uco = list(lista-apa)
ert=[]
l=0
for i in range(len(uco)):
    ut = []
    ut.append(data[uco[i]-2])
    v=0
    j=0
    while(v==0):
        if(data[ut[j]-2]==1):
            ert.append(j+2)
            v=1
            if(l<j+2):
                l=j+2
        else:
            ut.append(data[ut[j]-2])
            j=j+1
vege=[]
for i in range(len(uco)):
    if(ert[i]==l):
        vege.append(uco[i])
vege.sort()
print(len(vege),l)

print(" ".join([str(i) for i in vege]))

eredmeny=""
elso = True
for i in vege:
    if elso:
        elso=False
    else:
        eredmeny += " "
    eredmeny += str(i)
    
print (eredmeny)