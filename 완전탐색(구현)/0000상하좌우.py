#nxn의 격자 공간 1,1에서 출발하여 L,R,U,D 명령을 받아 도착한 곳의 좌표 출력

def left():
    global y
    if y<=1:
        return
    y=y-1

def right():
    global y
    if y>=n:
        return
    y=y+1

def up():
    global x
    if x<=1:
        return
    x=x-1

def down():
    global x
    if x>=n:
        return
    x=x+1

n=0
input_list=[]
n=int(input())
input_list=input().split()

#x,y좌표 선언
x,y=1,1
    
for command in input_list:
    if command=='L':
        left()
    elif command=='R':
        right()
    elif command=='U':
        up()
    else:
        down()

print(f'{x} {y}')