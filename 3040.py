import sys
def subset(cnt):
  if cnt==9:
    tmp=list();
    for i in range(9):
      if chk[i]:
        tmp.append(arr[i]);
    if sum(tmp)==100 and len(tmp)==7:
      for a in tmp:
        print(a);
    return
  chk[cnt]=True;
  subset(cnt+1);
  chk[cnt]=False;
  subset(cnt+1);

chk=[False]*9;
arr=list();
for _ in range(9):
  arr.append(int(sys.stdin.readline()));
subset(0)