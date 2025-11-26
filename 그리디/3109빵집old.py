#n열과 n+1열 검사하는 함수
r,c=map(int,input().split())
graph = [list(input()) for _ in range(r)]
vis=[[0]*(c+2) for _ in range(r+2)]
min_cnt=1e9

def inspect(n): #n열과 n+1열 비교
    global min_cnt
    cnt=0
    for i in range(r): #0~r-1행 순대로
        if graph[i][n]=='x': #x는 검사 안해도됨
            continue
        flag=0#오른쪽으로 가는 방법이 하나라도 있는지
        for j in range(-1,2): #-1,0,1 중 탐색한다
            if 0<=i+j<r: #범위밖 방지
                if graph[i+j][n+1]=='.' and vis[i+j][n+1]==1:
                    flag=1
                    break
        if flag:
            cnt+=1
            vis[i][n]=1

    #print(f'{n}열과{n+1}열을 비교한 결과, {cnt}개의 길이 보입니다.')
    min_cnt=min(min_cnt,cnt)

for i in range(r):
    vis[i][c-1]=1

for t in range(c-2,-1,-1): # c-1~>0 비교
    inspect(t)

print(min_cnt)