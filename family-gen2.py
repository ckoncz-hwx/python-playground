import sys
import random

if len(sys.argv)<3:
    print('please provide the family member count and MAX_CHILDREN the command line')
    sys.exit(1)

members = int(sys.argv[1])
MAX_CHILDREN =  int(sys.argv[2])

print(members)
candidate_parents=[1]
children={1:0}

for i in range(2,members+1):
    p = random.choice(candidate_parents)
    print(p)

    children[i]=0
    candidate_parents.append(i)

    children[p] += 1
    if children[p] == MAX_CHILDREN:
        candidate_parents.remove(p)
