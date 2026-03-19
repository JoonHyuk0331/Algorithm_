from collections import deque

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,k=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
s,out_x,out_y=map(int,input().split())
vis=[[0]*n for _ in range(n)]
q=deque()

for t in range(1,k+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j]==t:
                q.append((i,j))
                vis[i][j]=1

while q:
    x,y=q.popleft()
    if vis[x][y]>s: #지정된 초를 넘어가면 결과 출력
        print(graph[out_x-1][out_y-1])
        exit(0)

    for d in range(4):
        nx=x+dx[d]
        ny=y+dy[d]

        if nx<0 or nx>=n or ny<0 or ny>=n: #범위를 초과한다면
            continue
        if vis[nx][ny]:  # 방문한적 있다면
            continue
        q.append((nx,ny))
        graph[nx][ny]=graph[x][y]
        vis[nx][ny]=vis[x][y]+1

#딱 맞게 끝난경우
print(graph[out_x-1][out_y-1])
exit(0)

