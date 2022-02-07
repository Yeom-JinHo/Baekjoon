import sys

word=sys.stdin.readline().rstrip()
r=0;
c=0;
for i in range(1,len(word)):
  if(len(word)%i==0 and i<=len(word)/i):
    r=i;
    c=int(len(word)/i);
arr=[[0]*c for _ in range(r)]
i=0
for ci in range(c):
  for ri in range(r):    
    arr[ri][ci]=word[i];
    i+=1;
for ri in range(r):
  for ci in range(c):
    print(arr[ri][ci],end="")




