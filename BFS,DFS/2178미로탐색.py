"""
너무 기본이여서 할 말이 없음
"""

from collections import deque

n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input()))) #그래프 입력

vis=[[0]*m for _ in range(n)] #방문기록

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y)) # 튜플() 리스트[] 집합{}
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: #범위를 벗어나면
                continue
            if graph[nx][ny]==0: #벽이면
                continue
            if vis[nx][ny]==0: #간적 없다면
                graph[nx][ny]=graph[x][y]+1 #값 증가
                vis[nx][ny]=1 #방문표시
                q.append((nx,ny))

    return graph[n-1][m-1]

print(bfs(0,0))



