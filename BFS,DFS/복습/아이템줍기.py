"""
https://school.programmers.co.kr/learn/courses/30/lessons/87694

bfs인 척 하는 구현문제임
좌표 2배 아이디어
-1세팅 0칠하기 1 테두리 아이디어
"""

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 102 for _ in range(102)]  # 행: y // 열: x

    # 각 rec 에 대하여 2배해서 찍기
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda v:v*2,rec)
        # 좌표 찍기
        for y in range(y1, y2 + 1):  # 행
            for x in range(x1, x2 + 1):  # 열
                if y1<y<y2 and x1<x<x2: #테두리 내부 범위
                    graph[y][x]=0 # 배경칠하기
                elif graph[y][x]!=0: # 이미 칠해진곳은 건들지 않음
                    graph[y][x] = 1 # 선 칠하기

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    vis = [[0] * 102 for _ in range(102)]

    q = deque()
    q.append((characterX*2, characterY*2))
    vis[characterY*2][characterX*2] = 1
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            return vis[y][x]//2
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 < nx <= 100 and 0 < ny <= 100:
                if vis[ny][nx]==0 and graph[ny][nx]==1: #아직 안갔고,갈수있다면(1)
                    q.append((nx,ny))
                    vis[ny][nx]=vis[y][x]+1
    answer = 0
    return answer