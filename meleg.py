from sys import stdin, stdout

esor = [int(i) for i in stdin.readline().split()]
napok = [int(i) for i in stdin.readline().split()]
n = esor[0]
szam = napok.copy()
szam[0] = 0
szam[n-1] = 0
for m in range (n-2):
    if (napok[m+1]>napok[m] and napok[m+1]>napok[m+2]):
        szam[m+1]= 1
    else :
        if (napok[m+1]<napok[m] and napok[m+1]<napok[m+2]):
         szam[m+1] = 2
        else :
             szam[m+1] = 0
             print(napok[m],napok[m+1],napok[m+2],0)
print(szam)
out = 0
for o in range (n):
    kszam=0
    nszam=0
    for p in range (n-o-1):
        lista = []
        lista.append(szam[o])
        for q in range(p+1):
            lista.append(szam[o+q+1])
        nszam = lista.count(1)
        kszam = lista.count(2)
        if (nszam == esor[1] and kszam == esor[2]):
            out = out+1
stdout.write(str(out))