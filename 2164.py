import sys
from typing import Deque

q = Deque()
for i in range(int(sys.stdin.readline())):
    q.append(i+1)

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])
