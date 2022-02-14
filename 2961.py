import sys
def subset(cnt,sour,bit):
  if cnt == n :
    global result;
    if sour!=1 and bit!=0:
      result=min(result,abs(sour-bit))
    return
  
  subset(cnt+1,sour*arr[cnt][0],bit+arr[cnt][1]);
  subset(cnt+1,sour,bit);

n=int(sys.stdin.readline());
arr=list();
result=sys.maxsize;
for _ in range(n):
  arr.append(list(map(int,sys.stdin.readline().split())));
subset(0,1,0);
print(result)