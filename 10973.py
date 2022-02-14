import sys
def swap(a,b):
  tmp=arr[a];
  arr[a]=arr[b];
  arr[b]=tmp

def prevPer():
  i=N-1
  while i>0 and arr[i-1]<=arr[i]:
    i-=1
  if i==0:
    return False
  
  j=N-1
  while arr[i-1]<=arr[j]:
    j-=1
  
  swap(i-1,j)

  k=N-1
  while(i<k):
    swap(i,k)
    i+=1;
    k-=1;
  
  return True
    
N=int(sys.stdin.readline());
arr=list(map(int,sys.stdin.readline().split()))
if prevPer():
  for a in arr:
    print(a,end=" ")
  print()
else:
  print(-1)
