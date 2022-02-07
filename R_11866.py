import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split());

li=[i+1 for i in range(N)]
q=deque(li);
result=deque();
while q:
  for i in range(K-1):
    q.append(q.popleft());
  # q.rotate(-(K-1));
  result.append(q.popleft());

print(str(result).replace('[', '<').replace(']', '>'));