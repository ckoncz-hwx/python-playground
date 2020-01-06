import sys
from typing import List,Optional

N, M, K = (int(i) for i in sys.stdin.readline().split())

data: List[List[int]] = []

for j in range(N):
    row = [int(i) for i in sys.stdin.readline().split()]
    data.append(row)

# print (N,M,K)
# for i in range(N):
#     print(*data[i])

visited: List[List[int]] = []

def find_max_path(i: int,j: int) -> List[List[int]]:
    res: List[List[int]] = []
    res.append([i,j])
    visited.append([i,j])

    res1: List[List[int]] = []
    res2: List[List[int]] = []

    if j < M-1:
        if abs(data[i][j+1]-data[i][j]) <= K:
            if not [i,j+1] in visited:
                res1 = find_max_path(i, j+1)
    if i < N-1:
        if abs(data[i+1][j]-data[i][j]) <= K:
            if not [i+1, j] in visited:
                res2 = find_max_path(i+1,j)

    if len(res1) > len(res2):
        res = res + res1
    else:
        res = res + res2

    return res

max_len = 0
max_path = []
max_start = []

for i in range(N):
    for j in range(M):
        if [i,j] in visited:
            # we already have a path running through this node
            continue
        if max_len > (N-i-1)+(M-j-1):
            # we already have a path that is longer than the maximum possible starting from here
            continue
        p = find_max_path(i,j)
        if(len(p) > max_len):
            max_len = len(p)
            max_path = p
            max_start = [i,j]

# print(max_path)

print(max_len - 1)
print(*[i+1 for i in max_start])

p = max_path[0]
for i in range(1,max_len):
    pp = max_path[i]
    if pp[0] == p[0]:
        print('J', end='')
    else:
        print('L', end='')
    p = pp
print()