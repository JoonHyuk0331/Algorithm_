from copy import deepcopy

answer = []

def printg(g,title):
    print(f"===={title}====")
    for row in reversed(g):
        for col in row:
            print(col,end=" ")
        print()

def solution(n, build_frame):
    n+=1
    pillar=[[0]*n for _ in range(n)]
    floor=[[0]*n for _ in range(n)]
    def inspect(pil,flo):
        res=True
        for i in range(n): #y 행
            for j in range(n): #x 열
                if pil[i][j]: #(j,i)좌표에 pil 존재한다면 검사
                    #존재가능조건 검사: 바닥/기둥/보
                    if not (i==0 or pil[i-1][j] or flo[i][j] or flo[i][j-1]):
                        res=False
                if flo[i][j]:
                    #존재가능조건 검사: 좌기둥/우기둥/양쪽보
                    if not (pil[i-1][j] or pil[i-1][j+1] or (flo[i][j-1] and flo[i][j+1]) ):
                        res=False
        if res:
            print("검사통과")
        else:
            print("검사실패")
        return res

    for command in build_frame: #command[]: 0->x 1->y 2->기둥/보 3->삭제/설치
        x,y=command[0],command[1]
        print(f'{x},{y},{command[2]},{command[3]}')
        printg(pillar,"pillar전")
        printg(floor, "floor전")
        if command[3]:
            #1.그래프 -> temp (임시저장)
            temp_pillar,temp_floor=deepcopy(pillar),deepcopy(floor)
            #2.설치
            if command[2]:
                #보 설치
                floor[y][x]=1
            else:
                #기둥 설치
                pillar[y][x]=1
            #3.검사
            if not inspect(pillar,floor):
                pillar,floor=temp_pillar,temp_floor #검사통과하지 못하면 temp -> 그래프 (원복)
        else:
            #1.그래프 -> temp (임시저장)
            temp_pillar,temp_floor=deepcopy(pillar),deepcopy(floor)
            #2.삭제
            if command[2]:
                #보 삭제
                floor[y][x]=0
            else:
                #기둥 삭제
                pillar[y][x]=0
            #3.검사
            if not inspect(pillar,floor):
                pillar,floor=temp_pillar,temp_floor #검사통과하지 못하면 temp -> 그래프 (원복)
        printg(pillar,"pillar후")
        printg(floor, "floor후")

    for ii in range(n): # i 열
        for jj in range(n): # j 행
            if pillar[jj][ii]: #필러가 있으면
                answer.append([ii,jj,0])
            if floor[jj][ii]:
                answer.append([ii,jj,1])

    return answer

nn=5
bf=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(nn,bf))