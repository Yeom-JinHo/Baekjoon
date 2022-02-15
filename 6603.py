import sys
def comb(cnt,start,n):
  if cnt==6:
    for t in tmp:
      print(t,end=" ")
    print()
  else:
    for i in range(start,n):
      tmp[cnt]=num[i];
      comb(cnt+1,i+1,n)
while True:
  arr=list(map(int,sys.stdin.readline().split()))
  if arr[0]==0:
    break;
  num=arr[1:];
  tmp=[0]*6;
  comb(0,0,arr[0])
  print()
