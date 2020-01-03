import sys
from typing import List, Tuple, Dict, Any

print("enter species max age and fossil count")

max_age, fossil_count = (int(i) for i in sys.stdin.readline().split())

def time_key(time_stamp):
    return time_stamp['time']

time_data={}

def add_time_data(time_data: Dict[int, Any], key: str, time: int):
    if not time in time_data:
        time_data[time]={'time':time, 'start':0, 'end':0}
    time_data[time][key] += 1

for f in range(1,fossil_count+1):
    start, end = (int(i) for i in sys.stdin.readline().split())
    add_time_data(time_data, 'start', start)
    add_time_data(time_data, 'end', end)

print('data collected')

time_list = list(time_data.values())
time_list.sort(key=time_key, reverse=True)
print('data sorted')

time_list2 = []
for t in time_list:
    if t['start'] > 0 and t['end'] > 0:
        time_list2.append({
            'time': t['time'],
            'start': t['start'],
            'end': 0
        })
        time_list2.append({
            'time': t['time'],
            'start': 0,
            'end': t['end']
        })
    else:
        time_list2.append(t)

# print(time_list2)
print('data restructured')

first = True
start = None
count = 0
max = 0
max_intervals=[]

for t in time_list2:
    if first:
        first = False
        start = t['time']
        count = t['start']
        continue
    
    end = t['time']

    if count > max:
        max_intervals=[]
        max = count

    if count == max:
        max_intervals.append({'start': start, 'end': end})
    
    start = end
    count += t['start']
    count -= t['end']

print('max=', max, max_intervals)
