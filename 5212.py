import sys

dr=[0,0,-1,1];
dc=[1,-1,0,0];
R,C=map(int,sys.stdin.readline().split());

origin=list();

for _ in range(R):
  origin.append(list(sys.stdin.readline().rstrip()));
after=[[0]*C for _ in range(R)];

for r in range(R):
  for c in range(C):
    after[r][c]=origin[r][c];
minR=sys.maxsize;
maxR=0;
minC=sys.maxsize;
maxC=0;

for r in range(R):
  for c in range(C):
    if origin[r][c]=="X":
      count=0;
      for i in range(4):
        tr=r+dr[i];
        tc=c+dc[i];
        if tr>=0 and tr<R and tc>=0 and tc<C:
          if origin[tr][tc]==".":
            count+=1;
        else:
          count+=1;
      if count>=3:
        after[r][c]="."
      else:
        minR=min(r,minR);
        maxR=max(r,maxR);
        minC=min(c,minC);
        maxC=max(c,maxC);

for r in range(minR,maxR+1):
  for c in range(minC,maxC+1):
    print(after[r][c],end="")
  print()
      