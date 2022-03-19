from collections import deque
import sys

N,H,W =map(int,sys.stdin.readline().split());

arr=deque()
for _ in range(H):
  arr.append(list(sys.stdin.readline().rstrip()))
origin=["?"]*N;
for r in range(H):
  for c in range(0,N*W):
    if arr[r][c]!="?":
      origin[c//W]=arr[r][c];
for o in origin:
  print(o,end="")