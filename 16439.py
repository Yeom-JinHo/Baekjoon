import sys

def comb(ind,start):
  if ind==3:
    global answer;
    ans=0;
    for i in range(N):
      ans+=max(arr[i][combArr[0]],arr[i][combArr[1]],arr[i][combArr[2]]);
    answer=max(ans,answer)
  else:
    for i in range(start,M):
        combArr[ind]=i;
        comb(ind+1,i+1);
N,M =map(int,sys.stdin.readline().split());
answer=0;
arr=list();
chk=[False]*M;
combArr=[0]*3;
for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().split())));
comb(0,0);

print(answer);