import sys

def check(r,c):
  bCount=0;
  wCount=0;
  for i in range(8):
    for j in range(8):
      if board[i+r][j+c]==wBoard[i][j]:
        wCount+=1;
      if board[i+r][j+c]==bBoard[i][j]:
        bCount+=1;
  return wCount if wCount<bCount else bCount;


wBoard=['WBWBWBWB','BWBWBWBW',
        'WBWBWBWB','BWBWBWBW',
        'WBWBWBWB','BWBWBWBW',
        'WBWBWBWB','BWBWBWBW'];
bBoard=['BWBWBWBW','WBWBWBWB',
        'BWBWBWBW','WBWBWBWB',
        'BWBWBWBW','WBWBWBWB',
        'BWBWBWBW','WBWBWBWB'];

n,m=map(int,sys.stdin.readline().split());

board=list();
for r in range(n):
  board.append(sys.stdin.readline().rstrip());
minCount=9*9+1;
for r in range(n-7):
  for c in range(m-7):
      count=check(r,c);
      if minCount>count:
        minCount=count;
print(minCount)