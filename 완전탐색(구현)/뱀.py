from collections import deque

n=int(input())
k=int(input())
graph=[[0]*(n+2) for _ in range(n+2)]

#사과 입력
for i in range(k):
    x,y=map(int,input().split())
    graph[x][y]=2

#커맨드 입력
l=int(input())
command=['']*10002
for i in range(l):
    line=input().split()
    #print(line)
    s=int(line[0])
    c=line[1]
    command[s]=c

dx=[-1,0,1,0]
dy=[0,1,0,-1]
#초기상태
d=1 #0상 1우 2하 3좌
sec=0
x,y=1,1
q=deque()
q.append([1,1])

def turn_right():
    global d
    #print(f'방향{d}')
    d=(d+1)%4

def turn_left():
    global d
    #print(f'방향{d}')
    d=(d+3)%4

while True:
    sec+=1
    #print(f'{sec}초--------')
    nx=x+dx[d]
    ny=y+dy[d]
    #print(f'{nx},{ny}로 이동예정')
    if nx<=0 or nx>n or ny<=0 or ny>n:#벽
        #print("")
        break
    if graph[nx][ny]==1:#자기자신
        #print("자기자신")
        break
    if graph[nx][ny]!=2:#사과없으면
        a,b=q.popleft()
        graph[a][b]=0 # 꼬리 회수
        #print(f'꼬리회수({a},{b})')
    #최종이동처리
    #print(f"{nx},{ny}로 최종이동")
    x,y=nx,ny
    q.append([nx,ny])
    graph[nx][ny]=1
    #회전
    if command[sec]!='':
        #print("커맨드존재")
        if command[sec]=='L':
            #print("좌회전")
            turn_left()
        else:
            #print("우회전")
            turn_right()

print(sec)
