
import sys

tc=int(sys.stdin.readline());

for _ in range(tc):
  k,n=map(int,sys.stdin.readline().split())
  arr=list();
  for _ in range(4):
    arr.append(sorted(list(map(int,sys.stdin.readline().split()))))
  arr1=list();
  arr2=list();
  for a1 in arr[0]:
    for a2 in arr[1]:
      arr1.append(a1+a2);
  for a3 in arr[2]:
    for a4 in arr[3]:
      arr2.append(a3+a4);
  arr1=sorted(arr1);
  arr2=sorted(arr2);
  answer= sys.maxsize;
  start=0;
  end=n*n-1;
  while start<=end:
    tmp=arr1[start]+arr2[end];
    # print(start,end,arr1,arr2,tmp,answer)
    if abs(tmp-k)<abs(answer-k):
      answer=tmp;
    elif abs(tmp-k)==abs(answer-k):
      answer=min(tmp,answer);
    if tmp>k:
      end-=1;
    elif tmp<k:
      start+=1;
    else:
      break;
  # print(answer)
  start=0;
  end=n*n-1;
  while start<=end:
    tmp=arr2[start]+arr1[end];
    # print(start,end,arr2,arr1,tmp,answer)
    if abs(tmp-k)<abs(answer-k):
      answer=tmp;
    elif abs(tmp-k)==abs(answer-k):
      answer=min(tmp,answer);
    if tmp>k:
      end-=1;
    elif tmp<k:
      start+=1;
    else:
      break;
  print(answer)







