#각 층에 대하여

#땅으로 매우는게 나은지 확인한다(평가법: 현재 층에 땅 파내는 시간 vs 매우는 시간, 동일하면 땅을 매우는시간이 낫다고 평가)
 #땅으로 메울 수 있는 자원이 있는지 확인한다 (밑에층을 포함해서 땅으로 메울 블럭이 존재하는지)
 #땅으로 메우고 시간을 계산한다
 #종료

#불가능하면
 #삽으로퍼내고
 #블럭 추가한다
 #시간을 추가한다

import sys
input=sys.stdin.readline

n,m,b=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
result=99999999
result_floor=0

for floor in range(257):
    # 현재 floor 층으로 평탄화 작업이 가능한가?
    # 초기 블럭(b)+깎아서 얻은 블럭 >= 목표 층으로 만드는데 필요한 부족분 이면 가능
    new_block=0 # 깎아서 얻은 블럭 개수
    need_block=0 # 목표 층으로 만드는데 필요한 블럭 개수
    for i in range(n):
        for j in range(m):
            if board[i][j]>floor:
                new_block+=(board[i][j]-floor)
            else:
                need_block+=(floor-board[i][j])
    #print(new_block,need_block)
    if b+new_block>=need_block and result>=new_block*2+need_block:
        result=new_block*2+need_block
        result_floor=floor
print(result,result_floor)





