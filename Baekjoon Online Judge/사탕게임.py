n=int(input())
board=[list(input()) for _ in range(n)]
colors=['C','P','Z','Y']
#전수조사 세로 50 가로 50 색깔별 4
max_cnt=0

print(board)

for color in colors:
    # 세로
    print(f'세로={color}=')
    for c in range(n):
        cnt=1
        for r in range(n-1):
            print(f'board[{r}][{c}]')
            if board[r][c]==color:
                if board[r+1][c]==color:
                    cnt+=1
                    print(f'({r},{c})={board[r][c]} ({r+1},{c})={board[r+1][c]}')
                    max_cnt=max(max_cnt,cnt)
                else:
                    cnt=1
    print(f'가로={color}=')
    for r in range(n):
        cnt=1
        for c in range(n-1):
            print(f'board[{r}][{c}]')
            if board[r][c]==color:
                if board[r][c+1]==color:
                    cnt+=1
                    print(f'({r},{c})={board[r][c]} ({r},{c+1})={board[r][c+1]}')
                    max_cnt=max(max_cnt,cnt)
                else:
                    cnt=1

    print(max_cnt)