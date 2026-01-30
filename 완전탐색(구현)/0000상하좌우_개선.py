#nxn의 격자 공간 1,1에서 출발하여 L,R,U,D 명령을 받아 도착한 곳의 좌표 출력

#dx,dy
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_type=['L','R','U','D']

n=0
inputs=[]
n=int(input())
inputs=input().split()

#x,y좌표 선언
x,y=1,1

#input을 하나씩 확인
for input in inputs:
    #좌표이동
    for i in range(4):
        if input==move_type[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    
    #공간을 벗어나면 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue

    x,y=nx,ny

#print(f'{x} {y}')
print(x, y)