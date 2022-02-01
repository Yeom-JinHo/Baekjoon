import sys

N,K =map(int,sys.stdin.readline().split());

count=0;
li=[[0]*6 for _ in range(2)];
for _ in range(N):
  sex,year=map(int,sys.stdin.readline().split());
  li[sex][year-1]+=1;

for s in range(2):
  for y in range(6):
    if li[s][y]%K==0:
      count+=li[s][y]//K
    else:
      count+=li[s][y]//K+1
print(count)