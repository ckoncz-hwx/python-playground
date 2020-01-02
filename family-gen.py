import sys
import random

if len(sys.argv)<2:
    print('please provide the family member count on the command line')
    sys.exit(1)

members = int(sys.argv[1])
print(members)
for i in range(2,members+1):
    print(random.randint(1,i-1))
