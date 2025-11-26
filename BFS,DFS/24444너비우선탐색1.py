from collections import deque
import sys

input=sys.stdin.readline
n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)] # n+1 x n+1 배열만든다
vis=[0]*(n+1) # n+1 x n+1 배열만든다
cnt=2

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(t):
    global cnt
    q=deque()
    q.append(t)
    vis[t]=1
    while q:
        now=q.popleft()
        graph[now].sort()
        for cur in graph[now]:
            if vis[cur]==0:
                vis[cur]=cnt
                cnt+=1
                q.append(cur)

bfs(r)
for i in range(1,n+1):
    print(vis[i])