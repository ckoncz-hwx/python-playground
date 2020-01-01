from typing import List, Tuple

def find(start: List[int] = None):
    state = start.copy() if start else []
    row = len(state)
    if row > 7:
        row = 7
    while row < 8:
        success, pos  = calc_next_pos(state, row)
        if success:
            if len(state) == row+1:
                state[row] = pos
            else:
                state.append(pos)
            row += 1
        elif row > 0:
            state = state[0:row]
            row -= 1
        else:
            return None
    return state

def calc_next_pos(state: List[int], row: int) -> Tuple[bool, int]:
    pos = state[row] if len(state)==(row+1) else -1
    success = False
    while not success and pos < 7:
        pos += 1
        success = not collides(row, pos, state)
    return success, pos


def collides(row: int, pos: int, state: List[int]):
    for i in range(row):
        if collide(row, pos, i, state[i]):
            return True
    return False

def collide(y1: int, x1: int, y2: int, x2: int):
    if x1 == x2 or y1 == y2:
        return True
    elif abs(x1-x2)==abs(y1-y2):
        return True
    else:
        return False

l = find()
print(l)
for i in l:
    print(' '*i, end='')
    print('*')

solutions=[]
while(l):
    solutions.append(l)
    l = find(l)

print('solution count %d'%len(solutions))
