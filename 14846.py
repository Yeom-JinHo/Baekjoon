import sys

N= int(sys.stdin.readline());

inp =list();

for _ in range(N):
  inp.append([0]+list(map(int,sys.stdin.readline().split())));

arr=list();
arr.append([[0]*(N+1)]+inp);
for i in range(10):
  arr.append([[0]*(N+1) for _ in range(N+1)]);


for r in range(1,N+1):
  for c in range(1,N+1):
    arr[arr[0][r][c]][r][c]+=1;
    for i in range(1,11):
      arr[i][r][c]+=arr[i][r][c-1]+arr[i][r-1][c]-arr[i][r-1][c-1];

C=int(sys.stdin.readline());
for _ in range(C):
  sr,sc,er,ec=map(int,sys.stdin.readline().split());
  count=[0]*11;
  for i in range(1,11):
    count[i]+=arr[i][sr-1][sc-1];
    count[i]-=arr[i][sr-1][ec];
    count[i]-=arr[i][er][sc-1];
    count[i]+=arr[i][er][ec]
  
  answer=0;
  for c in count:
    if c>0:
      answer+=1;

  print(answer);
