from collections import deque

#구역의 개수을 어떻게 셀까? 각 칸을 스캔해서 방문안됐으면 vis=1로 만들고 bfs돌린다

n=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

board=[]
for i in range(n):
    board.append(list(input()))
vis=[[0]*n for _ in range(n)]

q=deque()

def bfsColor(x,y,color):
    q.append([x,y])
    vis[x][y]=1
    while q:
        #look()
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n : #범위 밖이거나 이미 방문 한 경우 제외
                continue
            if vis[nx][ny]==0 and board[nx][ny]==color: #방문한적 없고 이동 가능한 구역이면(color)
                vis[nx][ny]=1
                q.append([nx,ny])

def changeRedtoGreen():
    for i in range(n):
        for j in range(n):
            if board[i][j]=='R':
                board[i][j]='G'

def look():
    for i in range(n):
        for j in range(n):
            print(board[i][j],end='')
        print()
    print()

def lookVis():
    print("lookVis")
    for i in range(n):
        for j in range(n):
            print(vis[i][j],end='')
        print()
    print()

count=0
disorderCount=0

for i in range(n):
    for j in range(n):
        if vis[i][j]==0:
            color=board[i][j]
            count+=1
            if color=='R':
                #print("bfs Red 실시")
                bfsColor(i,j,'R')
            if color=='G':
                #print("bfs Green 실시")
                bfsColor(i,j,'G')
            if color=='B':
                #print("bfs Blue 실시")
                bfsColor(i,j,'B')

changeRedtoGreen()

vis=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if vis[i][j]==0:
            color=board[i][j]
            disorderCount+=1
            if color=='G':
                #print("bfs Green 실시")
                bfsColor(i,j,'G')
            if color=='B':
                #print("bfs Blue 실시")
                bfsColor(i,j,'B')
print(count,disorderCount,sep=' ')
