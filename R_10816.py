import sys

N=int(sys.stdin.readline());
nCard =list(map(int,sys.stdin.readline().split()));
M=int(sys.stdin.readline());
hasCard=list(map(int,sys.stdin.readline().split()));
count=[[0]*len(hasCard)];

for i in range(len(hasCard)):
  count[i]=nCard.count(hasCard[i])

print(count)

