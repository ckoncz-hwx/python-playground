from sys import stdin, stdout

elso = [int (i) for i in stdin.readline().split()]
x = int(stdin.readline())

ul=[]
rl=[0 for i in range(elso[0])]
rl[0]=elso[3]

for i in range(x):
    print(rl[0], sum(rl))
    
    magok = sum(rl[elso[1]-1:(elso[1]+elso[2]-1)])
    ul.append(magok)
    ul = ul + rl[0:-1]
    rl=ul
    ul=[]