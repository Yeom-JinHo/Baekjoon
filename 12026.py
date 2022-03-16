import sys
BOJ=['B','O','J'];
N=int(sys.stdin.readline());

arr=list(sys.stdin.readline().rstrip());

energy=[sys.maxsize] * N;

energy[0]=0;

for now in range(1,N):
  for prev in range(now-1,-1,-1):
    if BOJ[BOJ.index(arr[now])-1]==arr[prev] and energy[prev]!=sys.maxsize:
      energy[now]=min(energy[now],energy[prev]+(now-prev)*(now-prev));

if energy[N-1]==sys.maxsize:
  print(-1)
else:
  print(energy[N-1])
