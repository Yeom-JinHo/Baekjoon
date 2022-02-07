import sys

n,m=map(int,sys.stdin.readline().split());
dic=dict();
for i in range(n):
  input=sys.stdin.readline().rstrip();
  dic[input]=i+1;
  dic[i+1]=input;
for _ in range(m):
  q=sys.stdin.readline().rstrip();
  if(q.isalpha()):
    print(dic[q])
  else:
    print(dic[int(q)])