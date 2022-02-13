import sys
sys.setrecursionlimit(10**6);

def fac(n):
  if n<1:
    return 1
  return n*fac(n-1)

tc = int(sys.stdin.readline())

for _ in range(tc):
  N,M=map(int,sys.stdin.readline().split());
  answer=fac(M)//(fac(M-N)*fac(N))
  print(answer)