import sys
import random

if len(sys.argv) < 3:
    print("please specify species max age and species count on the command line")
    sys.exit(1)

max_age = int(sys.argv[1])
spec_count = int(sys.argv[2])
print(max_age, spec_count)

for i in range(spec_count):
    start = random.randint(1,max_age)
    end = random.randint(1,start)
    print(start, end)
