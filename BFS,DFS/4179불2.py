"""
불과 지훈이 '동시'에 움직였음을 어떻게 풀어낼까
-> 불의 자취로 지훈의 움직임이 제한되므로 불의 자취를 먼저 기록한다음
-> 지훈의 움직임 완전탐색한다
"""
from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(input()))

vis=[[0]*m for _ in range(n)]
fireGraph=[[-1]*m for _ in range(n)]

dx,dy=[1,-1,0,0],[0,0,1,-1]

q = deque()
q2= deque()
fireflag=False

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            q.append([i,j])
            vis[i][j]=1
        if graph[i][j] == 'F':
            fireflag=True
            q2.append([i,j])
            fireGraph[i][j]=1

def bfs():
    while q:
        x,y=q.popleft()
        if (x==0 or x==n-1 or y==0 or y==m-1): #탈출가능 구역
            return vis[x][y] #탈출: 정점의 값 출력
        for dir in range(4):
            #printGraph(graph,n,m,"맵 전체 상태")
            nx=x+dx[dir]
            ny=y+dy[dir]
                #printGraph(vis,n,m,"지훈vis")
                #print(f'({nx},{ny}) 지훈이가 탐색')
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]=='F': #불붙은곳이라면
                continue 
            if graph[nx][ny]=='.' and vis[nx][ny]==0 and (vis[x][y]+1)<fireGraph[nx][ny]: #갈 수 있고,아직 방문하지 않았고,불이 닿지 않았다면
                vis[nx][ny]=vis[x][y]+1 # 증가값은 vis 에 메모할것임
                q.append([nx,ny])
        #printGraph(vis,n,m,"지훈 vis")

    return "IMPOSSIBLE"

# fireGraph 정점에 몇번째로 불이 도달하는지 적음
def fireBfs():
    while q2:
        x,y=q2.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]!='#' and fireGraph[nx][ny]==-1: #갈 수 있고 아직 방문하지 않았다면
                fireGraph[nx][ny]=fireGraph[x][y]+1
                q2.append([nx,ny])
    #printGraph(fireGraph,n,m,"fireGraph")

# 불이 없는 경우를 고려
if fireflag==False:
    for i in range(n):
        for j in range(m):
            fireGraph[i][j]=99999999# 불이 99999999초 후에 붙는다고 처리해버림

fireBfs()
print(bfs())

#디버깅용
def printGraph(graph, n, m,title):
    print(f'==={title}===')
    for i in range(n):
        for j in range(m):
            print(f"{graph[i][j]:3}", end=" ")
        print()
    print()


        