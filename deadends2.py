import sys
from typing import Dict, Set, List

from sys import path

N, M = (int(i) for i in sys.stdin.readline().split())

data: Dict[int, Set[int]] = {}

def add_data(n1: int, n2: int):
    if not n1 in data:
        data[n1]=set()
    data[n1].add(n2)

for i in range(M):
    n1, n2 = (int(i) for i in sys.stdin.readline().split())
    add_data(n1, n2)
    add_data(n2, n1)

start_points: List[int]=[]

for n in data:
    if len(data[n]) == 1:
        start_points.append(n)

def get_path_len(n:int):
    pl = 1
    nn = list(data[n])[0]
    while True:
        paths = data[nn]
        if(len(paths)==2):
            pl += 1
            old_nn = nn
            nn = list(paths-{n})[0]
            n = old_nn
        else:
            break
    return pl
    

max_len = 0
recorders: List[int] = []

for n in start_points:
    path_len = get_path_len(n)
    if path_len > max_len:
        max_len = path_len
        recorders = []
    if path_len == max_len:
        recorders.append(n)

recorders.sort()
if len(recorders)==0:
    print(-1)
else:
    print(max_len)
    for n in recorders:
        print(n)
