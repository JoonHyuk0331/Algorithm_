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
visFire=[[0]*m for _ in range(n)]

dx,dy=[1,-1,0,0],[0,0,1,-1]

q = deque()
jihoon=None
fire=None

# 전체 그래프에서 시작점 찾기
# 시작점 큐에 넣기, 방문표시
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'J':
            jihoon=[i,j,'J']
            q.append(jihoon)
            vis[jihoon[0]][jihoon[1]] = 1
        if graph[i][j] == 'F':
            fire=[i,j,'F']
            q.append(fire)
            visFire[fire[0]][fire[1]] = 1

"""
고려대상
1.지훈의 경우 탈출조건 설정
2.증가값을 메모한다

"""
def bfs():
    while q:
        x,y,flag=q.popleft()
        if flag=='J' and (x==0 or x==n-1 or y==0 or y==m-1) and graph[x][y]=='.':
            return vis[x][y] #탈출: 정점의 값 출력
        for dir in range(4):
            nx=x+dx[dir]
            ny=y+dy[dir]
            if flag=='J': #지훈

                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue

                if graph[nx][ny]=='.' and vis[nx][ny]==0: #갈 수 있고 아직 방문하지 않았다면
                    vis[nx][ny]=vis[x][y]+1 # 증가값은 vis 에 메모할것임
                    q.append([nx,ny,'J'])

            else: #불
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue

                if graph[nx][ny]!='#' and visFire[nx][ny]==0: #갈 수 있고 아직 방문하지 않았다면
                    graph[nx][ny]='F' # 불태워버림
                    visFire[nx][ny]=1 # 증가값은 vis 에 메모할것임
                    q.append([nx,ny,'F'])

    return "IMPOSSIBLE"

print(bfs())

# 디버깅용
def printGraph(graph, n, m,title):
    print(f'==={title}===')
    for i in range(n):
        for j in range(m):
            print(f"{graph[i][j]:3}", end=" ")
        print()
    print()




        