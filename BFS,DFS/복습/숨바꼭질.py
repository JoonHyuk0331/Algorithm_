# 수빈이는 -1 +1 또는 *2 이동가능
# 수빈이가 동생에게 가는 경로를 bfs 하자

#bfs를 사용할것이므로
from collections import deque

n,k=map(int,input().split())
graph=[0]*100005
q=deque()
q.append(n)
graph[n]=1 #방문처리

#-1,+1,*2 경우의 수를 탐색
while q:
    cur=q.popleft()
    #동생을 찾았다
    if cur==k:
        print(graph[cur]-1)
    if 0<=cur+1<=100000 and graph[cur+1]==0:
        graph[cur+1]=graph[cur]+1
        q.append(cur+1)
    if 0<=cur-1<=100000 and graph[cur-1]==0:
        graph[cur-1]=graph[cur]+1
        q.append(cur-1)
    if 0<=cur*2<=100000 and graph[cur*2]==0:
        graph[cur*2]=graph[cur]+1
        q.append(cur*2)


