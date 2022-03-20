import sys
dr=[0,0,-1,1];
dc=[1,-1,0,0];
ac=list();
def spread(arr):
  tmp=[[0]*C for _ in range(R)]
  for r in range(R):
    for c in range(C):
      if arr[r][c]>0:
        count=0;
        for i in range(4):
          tr=r+dr[i];
          tc=c+dc[i];
          if tr>=0 and tr<R and tc>=0 and tc<C:
            if arr[tr][tc]!=-1:
              count+=1;
              tmp[tr][tc]+=arr[r][c]//5;
      
        tmp[r][c]-=(arr[r][c]//5)*count;
  for r in range(R):
    for c in range(C):
      arr[r][c]+=tmp[r][c]

def rotate(arr,sr,sc,top):
  if top:
    minR=0;
    maxR=sr+1;
    dr=[-1,0,1,0];
    dc=[0,1,0,-1];
  else:
    minR=sr;
    maxR=R;
    dr=[1,0,-1,0];
    dc=[0,1,0,-1];
  i=0;
  r=sr+dr[i];
  c=sc+dc[i];
  while True:
    tr=r+dr[i];
    tc=c+dc[i];
    if tr==sr and tc==sc:
      arr[r][c]=0;
      break;
    if tr>=minR and tr<maxR and tc>=0 and tc<C:
      arr[r][c]=arr[tr][tc];
      r=tr;
      c=tc;
    else:
      i=(i+1)%4;
R,C,T = map(int,sys.stdin.readline().split());

arr=list();

for _ in range(R):
  arr.append(list(map(int,sys.stdin.readline().split())));

for i in range(R):
  if arr[i][0]==-1:
    ac.append([i,0]);
    ac.append([i+1,0])
    break;

for i in range(T):
  spread(arr)
  rotate(arr,ac[0][0],ac[0][1],True);
  rotate(arr,ac[1][0],ac[1][1],False);

answer=0;
for r in range(R):
  for c in range(C):
    if arr[r][c]>0:
      answer+=arr[r][c]

print(answer)