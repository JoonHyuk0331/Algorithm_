from collections import deque

n=int(input())

dx=[0,0,1,-1]
dy=[1,-1,0,0]

# board=[]
# for i in range(n):
#     board.append(list(input())) 리스트 컴프리헨션 사용
board=[list(input()) for _ in range(n)]
vis=[[0]*n for _ in range(n)]

q=deque()

# def bfsColor(x,y,color):
#     q.append([x,y])
#     vis[x][y]=1
#     while q:
#         x,y=q.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx<0 or nx>=n or ny<0 or ny>=n :
#                 continue
#             if vis[nx][ny]==0 and board[nx][ny]==color:
#                 vis[nx][ny]=1
#                 q.append([nx,ny])

def bfs(x,y):
    q.append([x,y])
    vis[x][y]=1 # 이거 빠트려서 고생했음
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] #이렇게 and 조건으로 되는경우만 한번에 묶는것도 나쁘지 않다
            # 처음 큐에 들어간 색깔로 계속 할거니까 색깔비교 board[x][y] == board[nx][ny] 로 하는 아이디어
            if 0 <= nx < n and 0 <= ny < n and board[x][y] == board[nx][ny] and not vis[nx][ny]:
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
        if vis[i][j]==0: #if not vis[i][j]: 로 해도 좋음
            bfs(i,j)
            count+=1

changeRedtoGreen()

# 재 초기화는 그냥 한번 더 선언하는게 빠르다
vis=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            bfs(i,j)
            disorderCount+=1

print(count,disorderCount,sep=' ')
