import sys

sn=int(sys.stdin.readline());
arr=list(map(int,sys.stdin.readline().split()));
pn=int(sys.stdin.readline());
for _ in range(pn):
  gender,index=map(int,sys.stdin.readline().split())
  if(gender==1):
    for i in range(len(arr)):
      if((i+1)%index==0):
        arr[i]= 1 if arr[i]==0 else 0;
  else:
    arr[index-1]= 1 if arr[index-1]==0 else 0;
    # 일단 해당 인덱스 변경
    left=arr[0:index-1];
    right=arr[index-1:];
    for i in range(1,min(len(left),len(right)-1)+1):
      if(left[-i]==right[i]):
        left[-i]= 1 if left[-i]==0 else 0;
        right[i]= 1 if right[i]==0 else 0;
      else:
        break;
    arr=left+right
  
for i in range(0,len(arr),20):
  print(*arr[i:i+20]);