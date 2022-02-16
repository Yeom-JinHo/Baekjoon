import sys

def div(r,c,l):
  if l==1:
    result[arr[r][c]]+=1;
  else:
    t=arr[r][c]
    flag=True;
    for rr in range(l):
      for cc in range(l):
        if t!=arr[r+rr][c+cc]:
          flag=False;
    if flag:
      result[t]+=1;
    else:
      n=l//2;
      for i in range(2):
        for j in range(2):
          div(r+i*n,c+j*n,n)

N=int(sys.stdin.readline())

arr=list();

for _ in range(N):
  arr.append(list(map(int,sys.stdin.readline().split())));
result=[0,0]
div(0,0,N);
print(result[0]);
print(result[1])