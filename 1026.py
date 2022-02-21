import sys

# def perm(cnt):
#   if cnt==N:
#     global answer;
#     tmp=0;
#     for i in range(N):
#       tmp+=number[i]*b[i];
#     answer=min(answer,tmp);
#   else:
#     for i in range(N):
#       if not chk[i]:
#         chk[i]=True;
#         number[cnt]=a[i];
#         perm(cnt+1)
#         chk[i]=False;
N=int(sys.stdin.readline());
a=list(map(int,sys.stdin.readline().split()));
b=list(map(int,sys.stdin.readline().split()));
# number=[-1]*N;
# chk=[0]*N;
# perm(0);
a.sort()
b.sort(reverse=True);
answer=0;
for i in range(N):
  answer+=a[i]*b[i]
print(answer);