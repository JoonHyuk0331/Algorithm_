import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n,m,r=map(int,input().split())
graph=[[] for _ in range(n+1)] # n+1 x n+1 배열만든다
vis=[0]*(n+1) # n+1 x n+1 배열만든다
cnt=1

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(t):
    global cnt
    vis[t]=cnt
    graph[t].sort()
    for i in graph[t]:
        if vis[i]==0:
            cnt+=1
            dfs(i)

dfs(r)
for i in range(1,n+1):
    print(vis[i])