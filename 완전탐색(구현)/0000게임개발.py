#input
n,m=map(int,input().split()) #n은 세로 #m은 가로
x,y,dir=map(int,input().split())
x+=1
y+=1

#set board
board=[[0]*(m+1) for _ in range(n+1)] #board=[n+1][m+1]x
vis=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    board[i]=[0]+list(map(int,input().split())) #0육지,1바다

#북0,1 동1,0 남0,-1 서-1,0  (1,0)(0,1)(-1,0)(0,-1) 북동남서0123
dx=[0,1,0,-1,0,1,0,-1]
dy=[1,0,-1,0,1,0,-1,0]

def print_board():
    result=1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if(vis[i][j]==1):
                result+=1
            print(board[i][j],end="")
        print()
    return result

#반시계방향 탐색

def move():
    global x,y,dir
    next_dir=dir
    for i in range(next_dir,next_dir+4):
        print(f'debug: {x},{y}에서 빙빙 돕니다')
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<=0 and nx>=n+1 and ny<=0 and ny>=n+1:
            print(f'debug: 접근제한 구역 nx,ny={nx},{ny}')
            continue
        dir=next_dir%4 #방향전환
        print(f'debug: nx,ny={nx},{ny}')
        if board[nx][ny]==0 and vis[nx][ny]==0: #육지이고 아직 가보지 않았다면 전진
            x,y=nx,ny
            vis[x][y]=1
            return 1
        #가봤다면 다음방향 
    next_dir=next_dir-2 #방향 뒤로 
    nx=x+dx[next_dir]
    ny=y+dy[next_dir]
    if board[nx][ny] != 1: #뒤가 바다가 아니면 뒤로가기
        x,y=nx,ny
        vis[x][y]=1
        return 1
    
    return 0 #뒤로가도 바다면 break

#main
print(print_board())
while(move()):
    pass
print(print_board())
    
    
