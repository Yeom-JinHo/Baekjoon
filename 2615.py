import sys
def solution(r,c,color):
  for i in range(len(dr)):
    if check(r,c,i,color,1):
      if not check(r,c,(i+4)%8,color,5):
      # if not check(r,c,)
        return -1
      return i
  return -1;

def check (r,c,dir,color,count):
  if count==5:# 6알까지 검사하고 여섯번째도 포함이면 x 안포함이면 o
    tr=r+dr[dir];
    tc=c+dc[dir];
    if (tr>=0 and tc>=0 and tr<MAX_N and tc<MAX_N):
      if arr[r+dr[dir]][c+dc[dir]]==color:
        return False
    if arr[r][c]==color:
      return True
    else:
      return False
  tr=r+dr[dir];
  tc=c+dc[dir];
  if(tr>=0 and tc>=0 and tr<MAX_N and tc<MAX_N):
    if(arr[tr][tc]==color):
      if check(tr,tc,dir,color,count+1):
        return True;
      return False;
MAX_N=19;
# 좌측 상단부터 시계방향으로 돈다.
dr=[-1,-1,-1,0,1,1,1,0];
dc=[-1,0,1,1,1,0,-1,-1];
# 왼쪽 위부터 도니 우 우하 하만 고민하면 댐
# dr=[0,1,1]
# dc=[1,1,0]
arr=list();

for _ in range(MAX_N):
  arr.append(list(map(int,sys.stdin.readline().rstrip().split())));

for r in range(MAX_N):
  for c in range(MAX_N):
    if not arr[r][c]==0:
      resultDir=solution(r,c,arr[r][c])
      if not resultDir==-1:
          li=[[r,c]];
          for _ in range(4):
            li.append([r+dr[resultDir],c+dc[resultDir]]);
            r=r+dr[resultDir];
            c=c+dc[resultDir];
          li=sorted(li,key= lambda x: (x[1],x[0]))
          print(arr[r][c])
          print(li[0][0]+1,li[0][1]+1)
          sys.exit()
print(0)