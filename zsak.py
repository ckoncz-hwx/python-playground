from sys import stdin, stdout

n,m=(int (i) for i in stdin.readline().split())
utak = []
for i in range(m):
    utak.append([int (i) for i in stdin.readline().split()])

def find(p,n):
    w = []
    for i in range(m):
        if (p in utak[i] and not n in utak[i]):
           if ((utak[i][0]==p)):
               w.append(utak[i][1])
           else:
               w.append(utak[i][0])
    if (len(w)==1):
        return w[0]
    else:
        return 0

zsak = []
for i in range(n):
    s=0
    print('i=',i)
    for j in range(m):
        if (i+1 in utak[j]):
            s+=1
    if (s==1):
        zsak.append(i+1)
hossz=[-1 for i in range(len(zsak))]

for i in range(len(zsak)):
    e=zsak[i]
    r=0
    a=0
    while(not(e==0)):
        a=e
        e=find(e,r)
        hossz[i]+=1
        r=a
l=max(hossz)
vege=[]
for i in range(len(zsak)):
    if (hossz[i]==l):
        vege.append(zsak[i])
if (len(zsak)==0):
    print(-1)
else:
    print(l)   
    print(*vege)