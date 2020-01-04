import sys
import random
from typing import Dict, Set

if len(sys.argv)<3:
    print('please provide the village and road count on the command line')
    sys.exit(1)

vill_count, road_count = (int(i) for i in sys.argv[1:3])

print(vill_count, road_count)
data: Dict[int, Set[int]] = {}

def add_data(v1: int, v2: int):
    if not v1 in data:
        data[v1] = set()
    data[v1].add(v2)

for i in range(road_count):
    v1 = random.randint(1, vill_count)
    road_found = False
    v2 = 0
    while not road_found:
        v2 = random.randint(1, vill_count)
        if v2 == v1:
            continue
        elif v1 in data:
            if v2 in data[v1]:
                continue
        road_found = True
    add_data(v1,v2)
    add_data(v2,v1)
    print(v1,v2)
