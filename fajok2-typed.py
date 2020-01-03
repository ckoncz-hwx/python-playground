import sys
from typing import List, Dict
import enum

print("enter species max age and fossil count")

max_age, fossil_count = (int(i) for i in sys.stdin.readline().split())

#  no literal in 3.7 TimeDataKeys = Literal['time','start','end']

class TDK(enum.Enum):
    TIME =0
    START=1
    END=2

TimeDataEntry = Dict[TDK,int]
time_data: Dict[int, TimeDataEntry] ={}

def time_key(time_stamp: TimeDataEntry):
    return time_stamp[TDK.TIME]

def add_time_data(key: TDK, time: int):
    if not time in time_data:
        time_data[time]={TDK.TIME:time, TDK.START:0, TDK.END:0}
    time_data[time][key] += 1

for f in range(1,fossil_count+1):
    start, end = (int(i) for i in sys.stdin.readline().split())
    add_time_data(TDK.START, start)
    add_time_data(TDK.END, end)

print('data collected')

time_list = list(time_data.values())
time_list.sort(key=time_key, reverse=True)
print('data sorted')

time_list2: List[TimeDataEntry]= []
for t in time_list:
    if t[TDK.START] > 0 and t[TDK.END] > 0:
        time_list2.append({
            TDK.TIME: t[TDK.TIME],
            TDK.START: t[TDK.START],
            TDK.END: 0
        })
        time_list2.append({
            TDK.TIME: t[TDK.TIME],
            TDK.START: 0,
            TDK.END: t[TDK.END]
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
        start = t[TDK.TIME]
        count = t[TDK.START]
        continue
    
    end = t[TDK.TIME]

    if count > max:
        max_intervals=[]
        max = count

    if count == max:
        max_intervals.append({'start': start, 'end': end})
    
    start = end
    count += t[TDK.START]
    count -= t[TDK.END]

print('max=', max, max_intervals)
