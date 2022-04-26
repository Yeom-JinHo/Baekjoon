
import queue
import sys

class Edge:
  def __init__(self,a,b,w):
    self.a=a;
    self.b=b;
    self.w=w;
  
  def __lt__(self,other):
    return self.w<other.w; 

def union(a,b):
  aRoot = findParent(a)
  bRoot = findParent(b)
  if aRoot!=bRoot:
    parent[bRoot]=aRoot;
    return False;
  else:
    return True

def findParent(a):
  if parent[a]==a:
    return a
  parent[a]=findParent(parent[a])
  return parent[a];

N=int(sys.stdin.readline())
parent=[i for i in range(N+1)];

M=int(sys.stdin.readline())
pq=queue.PriorityQueue();
for _ in range(M):
  a,b,w=map(int,sys.stdin.readline().split());
  pq.put(Edge(a,b,w));

answer=0;
while not pq.empty():
  now =pq.get();
  if not union(now.a,now.b):
    answer+=now.w;

print(answer)