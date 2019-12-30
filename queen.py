koord = []
for i in range (8):
    for j in range (8):
        koord.append([i+1,j+1])
listak = []
for i in range (8):
    listak.append([])
    for j in range(8):
        listak[i].append([i+1,j+1])
for i in range (8):
    listak.append([])
    for j in range (8):
        listak[7+i].append([j+1,i+1])
for i in range (8):
    listak.append([])
    for j in range(8-i):
        listak[15+i].append([j+1,i+j+1])
for i in range(7):
    listak.append([])
    for j in range(7-i):
        listak[23+i].append([i+j+2,j+1])
for i in range(8):
    listak.append([])
    for j in range(8-i):
        listak[30+i].append([8-j,i+j+1])
for i in range(7):
    listak.append([])
    for j in range(7-i):
        listak[38+i].append([8-i-1-j,j+1])
listak.remove([])
print(listak)
 
 kerdes = []
 for i in range(8):
    kerdes.append(listak[0][i])
    for j