#문제입력받기
matrix=[[] for _ in range(4)]
for r in range(4):
    row=list(map(int,input().split()))
    for idx in range(0,8,2):
        matrix[r].append((row[idx],row[idx+1]))# (순서,방향)

#물고기 없는 칸 -> (0,0)
#상어가 지나간 칸 -> (99,0)

#물고기이동def
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

#물고기이동 def 행렬->변환된 행렬
def move_fish(now_matrix):
    # 1~16 번에 대해
    for target_fish_num in range(1,16+1):
        # 완전탐색하여 n 위치 좌표 찾기
        for x in range(0,4):
            for y in range(0,4):
                fish_num,fish_dir=now_matrix[x][y]
                if fish_num==target_fish_num:
                    # 위치바꾸기 실행
                    for i in range(8):
                        d=(fish_dir-1+i)%8 # 현재 물고기 방향에서 반시계
                        nx=x+dx[d]
                        ny=y+dy[d]
                        if now_matrix[nx][ny][0]==99: # 상어 칸으로는 이동할 수 없음
                            continue
                        if nx<0 or ny<0 or nx>=4 or nx>=4: # 경계 값
                            continue
                        if 1 <= now_matrix[nx][ny][0] <= 16: # 물고기 있으면 교환
                            now_matrix[x][y],now_matrix[nx][ny]=now_matrix[nx][ny],now_matrix[x][x]
                            break
                        if now_matrix[nx][ny][0]==0: # 물고기 없으면 이동
                            now_matrix[nx][ny]=now_matrix[x][y]
                            break
    #변환된 메트릭스 출력
    return now_matrix

#d 방향 0 index 주의
def dfs(x,y,d,now_matrix,cnt):
    cnt += now_matrix[x][y][0]
    for i in range(4):
        nx=x+dx[d]*i
        ny=y+dy[d]*i
        if nx < 0 or ny < 0 or nx >= 4 or nx >= 4:  # 경계 값
            continue
        if now_matrix[nx][ny]==(0,0): # 비어있는 칸
            continue
        # 물고기 먹기-먹기 전 상어가 있었던 자리 비어있게 처리
        now_matrix[x][y] = (0,0)
        dfs(nx,ny,now_matrix[nx][ny][1]-1,move_fish(now_matrix),cnt)


# debug=======================
def printg(g):
    for i in range(4):
        for j in range(4):
            print(g[i][j],end=" ")
        print()
# step 1 : move_fish 정상작동 확인

# step 2 : dfs 정상작동 확인