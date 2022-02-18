import sys

def per(cnt):
  global tmp;
  if(cnt==N):
    global answer;
    val=0;
    for i in range(N-1):
      val+=abs(tmp[i]-tmp[i+1]);
    answer=max(val,answer);
  else:
    for i in range(N):
      if not chk[i]:
        chk[i]=True;
        tmp[cnt]=arr[i];
        per(cnt+1);
        chk[i]=False;
N=int(sys.stdin.readline());
chk=[False]*N;
tmp=[0]*N;
arr=list(map(int,sys.stdin.readline().split()));
answer=0;
per(0);
print(answer)