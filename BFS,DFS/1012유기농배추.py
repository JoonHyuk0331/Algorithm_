"""
덩어리 찾는 유형
dfs 로 풀었음
"""

import sys
input = sys.stdin.readline #input보다 빠름 그러나 개행문자를 제거하지 않음
sys.setrecursionlimit(10**6) #재귀 제한 풀기

def dfs(x,y):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if (0<=nx<m) and (0<=ny<n) and graph[ny][nx]==1:
            graph[ny][nx]=-1 #방문완료
            dfs(nx,ny)

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split()) #가로,세로,심은 배추 개수
    graph=[[0]*m for _ in range(n)] #nxm행렬 세로n,가로m에 대응

    #배추 마킹
    for i in range(k):
        X,Y=map(int,input().split())
        graph[Y][X]=1


    ##카운팅
    count=0
    for i in range(m):#m 가로 x
        for j in range(n):#n 세로 y
            if graph[j][i]==1:
                dfs(i,j)
                count+=1
    print(count)

