from collections import deque
import sys
input = sys.stdin.readline # 개행문자를 자동으로 제거해주진 않지만 기본input과 다르게 빠르다
# 필요시 
# strip()은 문자열의 양쪽 끝에 있는 공백 문자(스페이스, 탭, 개행 등)을 제거
# s = sys.stdin.readline().strip()
# line = sys.stdin.readline().rstrip('\n')  # 공백이 포함된 문자에서 개행문자만 제거

m,n=map(int,input().split()) # 가로m 세로n
graph=[]
for _ in range(n):
    graph.append(list(map(int, input().split())))
#-> [ list(map(int, input().split())) for _ in range(n)] 으로도 가능

#선 push
#deque를 굳이 함수 내부에 선언할 필요 없다  
q = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def bfs():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: #범위 밖
                continue    
            if graph[nx][ny]==-1: #갈수 없는 곳
                continue
            if graph[nx][ny]==0: #아직 한번도 안 가본 곳
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))

            #이렇게 되는 경우를 and 조건으로 모아서 해도 된다
            # if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            # graph[nx][ny] = graph[x][y] + 1
            # queue.append((nx, ny)) # 큐에 새로운 토마토 위치 추가

def getResult():
    result=0
    for i in range(n):
        for j in range(m):
            tomato=graph[i][j]
            if tomato==0:
                return -1
                #함수로 쓰기 싫으면 exit() 도 있다
            result=max(result,tomato)
    return result-1

# for 문은 이렇게 해도 된다
# for line in arr:
#     for tomato in line:
#         if tomato == 0:
#             # 안익은 토마토(0)이 있으면 바로 정지
#             print(-1)
#             exit()
       
bfs()
print(getResult())




