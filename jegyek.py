from sys import stdin, stdout

n, k, l = (int (i) for i in stdin.readline().split())
hatar = [int (i) for i in stdin.readline().split()]
tanulo = [int (i) for i in stdin.readline().split()]
ujhatar=[]

for i in range(4):
    if (not (hatar[i] in tanulo)):
        ok=[]
        for j in range(l+1):
            if (hatar[i]-j-1 in tanulo):
                ok.append(1)
            else:
                ok.append(0)
        print(ok)
        jo=[]
        v0=0
        for k in range(l+1):
            if (ok[k]==1):
                jo.append(1)
            else:
                v0 = 1
                break
        if (v0 == 0):
            jo=[]
        print(jo)
        ujhatar.append(hatar[i]-len(jo))
    else:
        ujhatar.append(hatar[i])
print(ujhatar)