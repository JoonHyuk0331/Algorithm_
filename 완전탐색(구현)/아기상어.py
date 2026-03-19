from collections import deque

n = int(input())
m=n
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
level = 2
exp = 0
total_time = 0

def show_g():
    for iii in range(n):
        for jjj in range(n):
            print(board[iii][jjj],end=" ")
        print()

#시작좌표
#먹을수 있는 후보들의 좌표들 리스트
def bfs(a, b):
    #print(f'{a},{b}에서 bfs돌립니다')
    eatable_list=[]
    global level,exp
    vis = [[0] * m for _ in range(n)]
    q = deque([(a, b)])
    vis[a][b] = 1
    while q:
        x, y = q.popleft()
        #print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny]>level:
                    continue
                if vis[nx][ny]:
                    continue
                if 1<=board[nx][ny] < level:
                    eatable_list.append((nx,ny,vis[x][y]))

                q.append((nx, ny))
                vis[nx][ny] = vis[x][y] + 1
    return eatable_list
# 초기좌표찾기
st_x=0
st_y=0
for ii in range(n):
    for j in range(m):
        if board[ii][j]==9:
            st_x=ii
            st_y=j
            board[ii][j]=0

while True:
    e_list=bfs(st_x,st_y)
    if e_list:
        #최소거리 걸러내기
        e_list.sort(key=lambda x:(x[2], x[0], x[1]))
        x_pos,y_pos,time=e_list[0]
        #먹기
        exp += 1
        if exp == level:
            exp = 0
            level += 1
        total_time += time
        board[x_pos][y_pos] = 0  # 음식제거
        st_x,st_y=x_pos,y_pos
        #print(f'소요시간{total_time}')
        #show_g()

    else:
        print(total_time)
        break



