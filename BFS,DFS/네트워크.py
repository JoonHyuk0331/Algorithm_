# 인접 행렬에서 구현한 BFS
from collections import deque


def solution(n, computers):

    cnt=0
    vis = [False] * 201
    def bfs(v):
        q = deque()
        q.append(v)
        vis[v]=True
        while q:
            x = q.popleft()

            #인접 노드 탐색
            for nx in range(n):
                if not vis[nx] and computers[x][nx]:
                    q.append(nx)
                    vis[nx] = True

    for i in range(n):
        if not vis[i]:
            cnt+=1
            bfs(i)

    return cnt

graph=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]



solution(3,graph)