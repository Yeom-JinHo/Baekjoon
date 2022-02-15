import sys
def comb(cnt,start):
  if cnt ==L:
    vows=0;
    cons=0;
    for t in tmp:
      if t=='a' or t=='e' or t=='i' or t=='o' or t=='u':
        vows+=1;
      else:
        cons+=1;
    if vows>=1 and cons>=2:
      for t in tmp:
        print(t,end="")
      print()
  else:
    for i in range(start,C):
      tmp[cnt]=arr[i];
      comb(cnt+1,i+1)

L,C = map(int,sys.stdin.readline().split());
tmp=[0]*L;
arr=list(sys.stdin.readline().split());
arr.sort();
comb(0,0);
