import sys

n=int(sys.stdin.readline())

for _ in range(n):
  count,text=sys.stdin.readline().split()
  for t in text:
    print(t*int(count),end='')
  print()