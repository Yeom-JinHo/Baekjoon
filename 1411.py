from curses.ascii import islower
import sys

# 50*50*100 ? , 25000 << 2초 ? 

N=int(sys.stdin.readline());

arr=list();
for _ in range(N):
  arr.append(sys.stdin.readline().rstrip());
answer=0;
for left in range(N):
  for right in range(left+1,N):
    chkAlpha=[False]*26;
    tmp=arr[right];
    for k in range(len(arr[left])):
      # 변경되지 않은 값이라면
      if islower(tmp[k]):
        # 근데 변경할값이 쓸 수 없는 값이라면
        if chkAlpha[ord(arr[left][k])-ord("a")]:
          tmp=-1;
          break;
        else:
          chkAlpha[ord(arr[left][k])-ord("a")]=True;
          tmp=tmp.replace(tmp[k],arr[left][k].upper());
    if arr[left]==str(tmp).lower():
      answer+=1;

print(answer)
