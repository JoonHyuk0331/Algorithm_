n=int(input())
board=[list(input().rstrip()) for _ in range(n)]
colors=['C','P','Z','Y']
#전수조사 세로 50 가로 50 색깔별 4
max_cnt=0

def printg(g):
    for row in g:
        print(*row)

for color in colors:
    # 세로
    for c in range(n):
        cnt=1
        for r in range(n-1):
            if board[r][c]==color:
                if board[r+1][c]==color:
                    cnt+=1
                    max_cnt=max(max_cnt,cnt)
                else:
                    cnt=1
    for r in range(n):
        cnt=1
        for c in range(n-1):
            if board[r][c]==color:
                if board[r][c+1]==color:
                    cnt+=1
                    max_cnt=max(max_cnt,cnt)
                else:
                    cnt=1

for color in colors:
    # 세로 변경
    for c in range(n):
        for r in range(n-1):
            board[r][c],board[r+1][c]=board[r+1][c],board[r][c]
            #영향이 있었던 두 행에 대해서만 가로로 검사 r,r+1
            for rr in range(r,r+2):
                ccnt=1
                for cc in range(n-1):
                    if board[rr][cc]==color:
                        if board[rr][cc+1]==color:
                            ccnt+=1
                            max_cnt=max(max_cnt,ccnt)
                        else:
                            ccnt=1
            #영향이 있었던 열에 대해서 세로로 검사 c
            cccnt=1
            for rrr in range(n-1):
                if board[rrr][c]==color:
                    if board[rrr+1][c]==color:
                        cccnt+=1
                        max_cnt=max(max_cnt,cccnt)
                    else:
                        cccnt=1

            board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
    # 가로 변경
    for r in range(n):
        for c in range(n-1):
            board[r][c],board[r][c+1]=board[r][c+1],board[r][c]
            #영향이 있었던 두 열에 대해서만 세로로 검사 c,c+1
            for cc in range(c,c+2):
                ccnt=1
                for rr in range(n-1):
                    if board[rr][cc]==color:
                        if board[rr+1][cc]==color:
                            ccnt+=1
                            max_cnt=max(max_cnt,ccnt)
                        else:
                            ccnt=1
            board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]
            #영향이 있었던 행에 대해서 가로로 검사 r
            cccnt=1
            for ccc in range(n-1):
                if board[r][ccc]==color:
                    if board[r][ccc+1]==color:
                        cccnt+=1
                        max_cnt=max(max_cnt,cccnt)
                    else:
                        cccnt=1

print(max_cnt)