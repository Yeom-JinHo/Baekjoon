import sys

def findPipe(r,c):
  if(c==C-1):
    global answer
    answer+=1;
    return True;
  else:
    for i in range(3):
      tr=r+dr[i];
      tc=c+dc[i];
      if tr>=0 and tc>=0 and tr<R and tc<C:
        if arr[tr][tc]=='.':
          arr[tr][tc]=answer
          if findPipe(tr,tc):
            return True;
  return False
R,C=map(int,sys.stdin.readline().split());
arr=list();
dr=[-1,0,1];
dc=[1,1,1];
answer=0;
for _ in range(R):
  arr.append(list(sys.stdin.readline().rstrip()))
for i in range(R):
  findPipe(i,0);
print(answer);

