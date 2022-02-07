import sys

def back(index,n,m):
  if index==m:
    print(' '.join(map(str,li)));
    return
  else:
    for i in range(n):
      if not check[i]:
        check[i]=True;
        li.append(i+1);
        back(index+1,n,m);
        check[i]=False;
        li.pop();


n,m=map(int,sys.stdin.readline().split());
li=list();
check=[False]*n;
back(0,n,m);


