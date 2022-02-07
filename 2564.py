import sys

cl,rl =map(int,sys.stdin.readline().split()); # 가로 세로 길이
dr=0
dc=0; # 동근이 좌표 
n= int(sys.stdin.readline());
storeLi=list();
result=0;
for i in range(n+1):
  direction,distance=map(int,sys.stdin.readline().split());
  if(direction==1):
    r=0;
    c=distance;
  elif(direction==2):
    r=rl;
    c=distance;
  elif(direction==3):
    r=distance;
    c=0;
  elif(direction==4):
    r=distance;
    c=cl;
  if(i==n):
    dr=r;
    dc=c;
  else:
    storeLi.append([r,c])
for store in storeLi:
  sr=store[0];
  sc=store[1];
  if(abs(sr-dr)==rl): # 반대편에 있다면 남 북
    tmpDistance=rl+sc+dc;
  elif(abs(sc-dc)==cl):
    tmpDistance=cl+sr+dr;
  else: 
    tmpDistance=abs(sr-dr)+abs(sc-dc);
  result+= min(tmpDistance,2*(rl+cl)-tmpDistance)
print(result)
