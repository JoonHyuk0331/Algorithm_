import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

t=int(input())

def dfs(x,y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]
        # 장소검사: 범위,유효
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
            graph[nx][ny]=-1
            dfs(nx,ny)


for i in range(t):
    n,m,k=map(int,input().split())
    graph=[[0]*m for _ in range(n)]
    cnt=0

    #배추마킹
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a][b]=1

    #각 자리마다 dfs 돌리기
    for a in range(n):
        for b in range(m):
            if graph[a][b]==1:
                dfs(a,b)
                cnt+=1
    print(cnt)