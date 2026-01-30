import sys
N,M,R=map(int,input().split())
matrix=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
vis=[[0]*M for _ in range(N)]

def show_matrix(m):
    for i in range(N):
        for j in range(M):
            print(m[i][j],end=" ")
        print()

def rotate_circle(a,b):
    prev_val=matrix[a][b]
    for i in range(1+a,N-a):
        prev_val,matrix[i][a]=matrix[i][a],prev_val #좌측라인 하향
    for i in range(1+a,M-a):
        prev_val,matrix[N-a-1][i]=matrix[N-a-1][i],prev_val #밑쪽라인 우향
    for i in range(1+a,N-a):
        prev_val,matrix[N-i-1][M-a-1]=matrix[N-i-1][M-a-1],prev_val #우측라인 상향
    for i in range(1+a,M-a):
        prev_val,matrix[a][M-i-1]=matrix[a][M-i-1],prev_val #위쪽라인 좌향

for _ in range(R):
    for v in range(min(N,M)//2):
        rotate_circle(v,v)

show_matrix(matrix)

