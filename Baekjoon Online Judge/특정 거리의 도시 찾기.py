from collections import deque
import sys

input=sys.stdin.readline

# 결과값에서 1 뺴야함 시작값을 1로 시작해서그럼

N,M,K,X=map(int,input().split())
ans=[]
graph=[[] for _ in range(N+1)]
vis=[0]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)

def bfs(v):
    q=deque()
    q.append(v)
    vis[v]=1
    while q:
        cur=q.popleft()
        if vis[cur]==K+1:
            ans.append(cur)

        for nx in graph[cur]:
            if not vis[nx]:
                q.append(nx)
                vis[nx]=vis[cur]+1

bfs(X)
ans.sort()
if ans:
    for num in ans:
        print(num)
else:
    print(-1)