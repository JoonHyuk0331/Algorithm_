from collections import deque
import copy

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
max_safety_area=0

dx=[0,1,0,-1]
dy=[1,0,-1,0]

#삼중포문으로 벽치기
#bfs돌려서 안전영역 구하기
#최솟값 갱신

def show_g(g):
    for iii in range(n):
        for jjj in range(m):
            print(g[iii][jjj],end=" ")
        print()

def bfs(a,b):
    q=deque([(a,b)])
    vis[a][b]=True
    while q:
        x,y=q.popleft()
        for d in range(4):
            nx=x+dx[d]
            ny=y+dy[d]
            if 0<=nx<n and 0<=ny<m:
                if vis[nx][ny]==False and new_board[nx][ny]==0:
                    q.append((nx,ny))
                    vis[nx][ny]=True
                    new_board[nx][ny]=2

def count_safe_area(board_copy):
    cnt=0
    for ii in range(n):
        for jj in range(m):
            if board_copy[ii][jj]==0:
                cnt+=1
    return cnt

coord_list=[(x,y) for x in range(n) for y in range(m)]
coord_len=len(coord_list)

#버블 정렬을 떠올리시오
for i in range(coord_len):
    for j in range(i+1,coord_len):
        for k in range(j+1,coord_len):
            # p1,p2,p3인 점을 기준으로 한 포인트 잡기
            vis = [[0] * m for _ in range(n)] # 각 점 경우의 수 마다 초기화
            p1=coord_list[i]
            p2=coord_list[j]
            p3=coord_list[k]
            if board[p1[0]][p1[1]]!=0:
                continue
            if board[p2[0]][p2[1]]!=0:
                continue
            if board[p3[0]][p3[1]]!=0:
                continue
            #board를 카피하고 p1,p2,p3넣기 그리고 bfs돌리기
            new_board=copy.deepcopy(board)
            new_board[p1[0]][p1[1]] = 1
            new_board[p2[0]][p2[1]] = 1
            new_board[p3[0]][p3[1]] = 1
            #print(f"{i},{j},{k} 시작전======")
            #show_g(new_board)
            for aa in range(n):
                for bb in range(m):
                    if new_board[aa][bb]==2:
                        bfs(aa,bb)
            #print(f"{i},{j},{k} bfs진행 후----")
            #show_g(new_board)
            max_safety_area=max(max_safety_area,count_safe_area(new_board))
print(max_safety_area)



