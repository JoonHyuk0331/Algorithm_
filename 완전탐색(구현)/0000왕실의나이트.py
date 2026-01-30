input=str(input())
x=ord(input[0])-97
y=int(input[1])

dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]

count=0
for i in range(8):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<1 or nx>8 or ny<1 or ny>8:
        continue
    count+=1

print(count)
