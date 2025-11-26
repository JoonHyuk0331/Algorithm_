#각 행에 대해서 bfs를 실행한다
from collections import deque

r,c=map(int,input().split()) #r행c열
graph = [list(input()) for _ in range(r)]
vis=[[0]*(c+2) for _ in range(r+2)]

dx=[1,0,-1]#행에 해당

def dfs(x,y):
    #print(f'{x},{y}에서 dfs 돌립니다.')
    stk=[[x,y]]
    while stk:
        x,y=stk.pop()
        vis[x][y] = True
        #print(f'({x},{y})')
        if y==c-1:#끝에 도달함
            #print(f'success: {x},{y}에 도달.')
            return 1
        for d in range(3):
            nx,ny=x+dx[d],y+1
            if 0<=nx<r and 0<=ny<c and graph[nx][ny]=='.' and not vis[nx][ny]:
                stk.append([nx,ny])
                #vis[nx][ny]=True
                #break # 핵심코드
    #print(f'fail: 도달하지 못함.')
    return 0

cnt=0
for i in range(r):
    if dfs(i,0):
        cnt+=1

print(cnt)
