import sys
from typing import Deque

n = int(sys.stdin.readline())
que = Deque()
result = []
for _ in range(n):
    line = sys.stdin.readline().rstrip().split()
    if line[0] == 'push_back':
        que.append(line[1])
    elif line[0] == 'push_front':
        que.appendleft(line[1])
    elif line[0] == 'pop_front':
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que.popleft())
    elif line[0] == 'pop_back':
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que.pop())
    elif line[0] == 'size':
        result.append(len(que))
    elif line[0] == 'empty':
        if len(que) == 0:
            result.append(1)
        else:
            result.append(0)
    elif line[0] == 'front':
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que[0])
    elif line[0] == 'back':
        if len(que) == 0:
            result.append(-1)
        else:
            result.append(que[-1])

for re in result:
    print(re)
