"""
000
100
222 이런 거는 입력받을때 리스트화해서 append하자


"""

from collections import deque

n=int(input())
board=[[0]*n for _ in range(n)]
vis=[[0]*n for _ in range(n)]
for i in range(n):
    li=input()
    for j in range(n):
        board[i][j]=int(li[j])

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    count=1
    q=deque()
    q.append([x,y])
    vis[x][y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 범위
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if board[nx][ny]==1 and vis[nx][ny]==0:
                q.append([nx,ny])
                vis[nx][ny]=1
                count+=1
    ans.append(count)

ans=[]
for i in range(n):
    for j in range(n):
        if vis[i][j]==0 and board[i][j]==1: #이거 까먹지 말기
            bfs(i,j)

ans.sort()
print(len(ans))
for i in ans:
    print(i)


