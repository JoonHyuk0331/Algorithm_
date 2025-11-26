from collections import deque
# deque는 기본적으로 append,pop으로 오른쪽 입구만 열려있음
# appendleft,popleft로 왼쪽 입구도 조작가능
# append + popleft 또는 appendleft + pop 조합으로 큐 처럼 사용

#bfs메서드 정의
def bfs(graph,start,vis):
    q=deque([start])
    
    vis[start]=True
    while q:
        v=q.popleft()
        print(v,end='') # 방문 정점 출력
        for i in graph[v]:
            if not vis[i]: # 방문한적 없는 정점이라면
                q.append(i)
                vis[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

vis=[False]*9
bfs(graph,1,vis)

