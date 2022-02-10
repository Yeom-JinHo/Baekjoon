import sys
sys.setrecursionlimit(10**5)

def dfs(r,c,color):
    visted[r][c]=True;
    for i in range(4):
        tr=r+dr[i];
        tc=c+dc[i];
        if tc>=0 and tc<l and tr>=0 and tr<l:
            if not visted[tr][tc]:
                if graph[tr][tc]==color:
                    dfs(tr,tc,color)
    
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

l=int(sys.stdin.readline());
graph = []
for _ in range(l):
    graph.append(list(sys.stdin.readline().rstrip()));

visted = [[False]*l for _ in range(l)]

count1=0;
for r in range(l):
    for c in range(l):
        if not visted[r][c]:
            dfs(r,c,graph[r][c])
            count1+=1;

for r in range(l):
    for c in range(l):
        if graph[r][c]=='R':
            graph[r][c]='G';

visted = [[False]*l for _ in range(l)]
count2=0
for r in range(l):
    for c in range(l):
        if not visted[r][c]:
            dfs(r,c,graph[r][c])
            count2+=1;

print(count1,count2)
