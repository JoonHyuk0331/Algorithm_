from collections import deque

m,n=map(int,input().split()) # 가로m 세로n
graph=[]
starts=[]

for i in range(n):
    nums=list(map(int,input().split()))
    idx=0
    for num in nums:
        if num==1:
            starts.append((i,idx))
            #print(f'start: ({n},{idx})')
        idx+=1
    graph.append(nums)

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs(list):
    q=deque()
    for tu in list:
        q.append(tu)
    while q:
        x,y=q.popleft()
        #print(f'popleft: ({x},{y})')
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: #범위 밖
                continue    
            if graph[nx][ny]==-1: #갈수 없는 곳
                continue
            if graph[nx][ny]==0: #아직 한번도 안 가본 곳
                #print(f'graph[{x}][{y}]주변탐색: ({nx},{ny})->({graph[nx][ny]})')
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))

def getResult():
    result=0
    for i in range(n):
        for j in range(m):
            #print(f'({i},{j}): {graph[i][j]}')
            tomato=graph[i][j]
            if tomato==0:
                return -1
            result=max(result,tomato)
    return result-1
       
bfs(starts)
print(getResult())




