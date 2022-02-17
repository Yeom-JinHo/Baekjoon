import sys
def fac(n):
  if n<2:
    return 1;
  else:
    return n*fac(n-1);

def findCombByIndex(ind):
  if ind==N:
    return;
  next=(arr[1]-1)//fac(N-(ind+1))%(N-ind)
  count=0;
  for i in range(N):
    if chk[i]:
      continue;
    else:
      if count==next:
        answer.append(i+1);
        chk[i]=True;
        break;
      else:
        count+=1;
  findCombByIndex(ind+1)

def findIndexByComb(comb,ind):
  if ind==N:
    return
  cnt=0;
  for i in range(N):
    if chk[i]:
      continue
    else:
      if comb[ind]==i+1:
        chk[i]=True;
        break;
      else:
        cnt+=1;
  answer.append(answer.pop()+cnt*fac(N-(ind+1)));
  findIndexByComb(comb,ind+1);


N=int(sys.stdin.readline());
chk=[False]*N;
arr=list(map(int,sys.stdin.readline().split()));
answer=list();
if arr[0]==1:
  findCombByIndex(0);
  for r in answer:
    print(r,end=" ")
  print()
elif arr[0]==2:
  answer.append(0)
  findIndexByComb(arr[1:],0);
  print(answer.pop()+1)