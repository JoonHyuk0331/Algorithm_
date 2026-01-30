from collections import deque


def solution(maps):
    n = len(maps) #5
    m = len(maps[0]) #5
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    vis = [[0] * 101 for _ in range(101)]

    q = deque()
    q.append((0, 0))
    vis[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            return vis[x][y]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not 0 <= nx < n or not 0 <= ny < m: #범위를 벗어남
                continue
            if vis[nx][ny] != 0 or maps[nx][ny]==0: #이미 방문했거나 갈 수 없음
                continue
            q.append((nx, ny))
            vis[nx][ny] = vis[x][y]+1
    return -1
maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))