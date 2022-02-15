import copy
import sys


def solve(inputArr,cnt):
  arr=[[0]*N for _ in range(N)];
  for r in range(N):
    for c in range(N):
      arr[r][c]=inputArr[r][c]%1000;
  if cnt==1:
    return arr;
  else:
    to=solve(arr,cnt//2);
    if cnt%2==0:
      return arrMul(to,to);
    else:
      return arrMul(arrMul(to,to),arr);
def arrMul(arr1,arr2):
  tmp=[[0]*N for _ in range(N)];
  for r in range(N):
    for c in range(N):
      sum=0;
      for i in range(N):
          sum+=arr1[r][i]*arr2[i][c];
      tmp[r][c]=sum%1000;
  return tmp;

N,B = map(int,sys.stdin.readline().split());
input=list();
for _ in range(N):
  input.append(list(map(int,sys.stdin.readline().split())));

result=solve(input,B);
for i in range(N):
  for j in range(N):
    print(result[i][j],end=" ")
  print()