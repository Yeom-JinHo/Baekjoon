from collections import deque
from errno import EPROTONOSUPPORT
import sys

def quad(dep,r,c):
  if dep==1:
    result.append(arr[r][c]);
  else:
    type=arr[r][c];
    flag=True;
    for rr in range(r,r+dep):
      for cc in range(c,c+dep):
        if type!=arr[rr][cc]:
          flag=False;
    if flag:
      result.append(type);
    else:
      result.append("(");
      quad(dep//2,r,c);
      quad(dep//2,r,c+dep//2);
      quad(dep//2,r+dep//2,c);
      quad(dep//2,r+dep//2,c+dep//2);
      result.append(")")


N=int(sys.stdin.readline());
arr=list();
result=deque();
for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().rstrip())))
quad(N,0,0);

while result:
  print(result.popleft(),end="")