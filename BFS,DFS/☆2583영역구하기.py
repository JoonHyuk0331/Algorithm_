"""
가로 세로 설정 헷갈리지 말자
"""

from collections import deque

n,m,k=map(int,input().split()) # n세로 m가로 k 개수 5 7 3
ans=[]
board=[[0]*m for _ in range(n)] #배열 board[n새로축][m가로축] 만든다
vis=[[0]*m for _ in range(n)]
"""원래는 이렇게 하면 되는데
 0 1 2 3 4 5 6 n
0a b c d e f 
1
2
3
4
m
abcde접근은
for i in 세로범위
    for j in 가로범위
        board[i][j] 
        # i가 y범위고 j가 x범위이다 좌표평면에 정확하게 접근해야 할 경우 헷갈리지 말자
"""

"""이 문제는 좌표평면이라
m
4
3
2
1
0a b c d e f
 0 1 2 3 4 5 6 n
abcde접근은
for i in 세로범위
    for j in 가로범위
        board[i][j]
"""
for _ in range(k):
    #print("---")
    x1,y1,x2,y2=map(int,input().split())
    for i in range(y1,y2): #새로범위
        for j in range(x1,x2): #가로범위
            board[i][j]=1

# for i in range(n-1,-1,-1): #새로범위 접근
#     for j in range(m): #가로범위 접근
#         print(board[i][j],end=" ")
#     print()

dx=[1,-1,0,0]
dy=[0,0,1,-1]
#bfs
def bfs(x,y):
    count=1
    if vis[y][x]==1 or board[y][x]==1: #이미 방문했거나 방문 할 수 없는곳이면
        return
    q=deque()
    q.append([x,y])
    vis[y][x]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #범위 내부,
            if 0<=nx<m and 0<=ny<n:
                if board[ny][nx]==0 and vis[ny][nx]==0:#갈수있는(0),방문한적없는
                    q.append([nx,ny])
                    vis[ny][nx]=1
                    count+=1
    ans.append(count)

def printvis():
    #print("printvis")
    for i in range(n - 1, -1, -1):  # 새로범위 접근
        for j in range(m):  # 가로범위 접근
            print(vis[i][j], end=" ")
        print()

#모든 좌표평면에 대하여 bfs
for i in range(m): #x 0~6
    for j in range(n): #y 0~4
        bfs(i,j)
ans.sort()
print(len(ans))
print(*ans)#언페킹