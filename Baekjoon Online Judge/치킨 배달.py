#엣지케이스 처리

#각 1에서 bfs 돌린다
#기억 메모리에 (좌표,최단거리) append해서 저장한다
#기억 메모리에 최단거리 합 순으로 m만큼 순서대로 배치한다.
#빼낸거에서 좌표값,최대단거리에서 같은 좌표값끼리는 최단거리가 가장 짧은거 하나만 남겨놓는다
from collections import deque
from collections import defaultdict

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
dist_mem=[[[] for _ in range(n)] for _ in range(n)]
dist_sum=[[0]*n for _ in range(n)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def show_graph(g):
    for row in g:
        print(*row)
def show_valid(g):
    for row in g:
        for c in row:
            if c:
                print(c)

def bfs(a,b):
    vis=[[0]*n for _ in range(n)]
    q=deque([(a,b)])
    vis[a][b]=1
    while q:
        x,y=q.popleft()
        if board[x][y]==2:
            dist_mem[x][y].append([a,b,vis[x][y]])
            dist_sum[x][y]+=vis[x][y]
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                if vis[nx][ny]==0:
                    q.append((nx,ny))
                    vis[nx][ny]+=vis[x][y]+1

for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            bfs(i,j)

#기억 메모리에 최단거리 합 순으로 m만큼 순서대로 배치한다.
most_useful_store=[]
for i in range(n):
    for j in range(n):
        if dist_sum[i][j]:
            most_useful_store.append((i,j,dist_sum[i][j]))
most_useful_store.sort(key=lambda x:x[2])
most_useful_store=most_useful_store[:m]
#most_useful_store의 좌표에 저장된 값은 남겨져 있는 치킨집의 좌표이다.
#그 좌표에 해당하는 dist_mem 의 값 내부에 저장된 집 좌표를 모조리 집어넣는다
#만약 동일 집 좌표가 여러개면 그 중 상점까지의 거리가 가장 짧은 거리를 가진 집 좌표를 대표로 넣는다
dic=defaultdict(lambda: 9999)
for data in most_useful_store:
    pos_x,pos_y,dist=data
    for home_data in dist_mem[pos_x][pos_y]:
        if home_data:
            home_x,home_y,home_to_store_dist=home_data
            dic[(home_x,home_y)]=min(dic[(home_x,home_y)],home_to_store_dist)

print(most_useful_store)
print(dic)

mindist_sum=0
for key in dic:
    mindist_sum+=(dic[key]-1)

print(mindist_sum)