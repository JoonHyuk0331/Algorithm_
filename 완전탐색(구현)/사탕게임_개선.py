n=int(input())
board=[list(input().rstrip()) for _ in range(n)]
colors=['C','P','Z','Y']
#전수조사 세로 50 가로 50 색깔별 4
max_cnt=0

# 해당 행에서 가장 많이 붙어있는 색에 대해 max 값 갱신
def row_max(row_idx):
    global max_cnt
    for colo in colors:
        ans = 1
        for col in range(n-1):
            if board[row_idx][col]==colo and board[row_idx][col+1]==colo:
                ans+=1
            else:
                ans=1
            max_cnt=max(max_cnt,ans)

def col_max(col_idx):
    global max_cnt
    for colo in colors:
        ans = 1
        for row in range(n-1):
            if board[row][col_idx]==colo and board[row+1][col_idx]==colo:
                ans+=1
            else:
                ans=1
            max_cnt=max(max_cnt,ans)

for c in range(n):
    col_max(c)

for r in range(n):
    row_max(r)

for color in colors:
    # 세로 변경
    for c in range(n):
        for r in range(n-1):
            board[r][c],board[r+1][c]=board[r+1][c],board[r][c]
            row_max(r)
            row_max(r+1)
            col_max(c)
            board[r][c], board[r + 1][c] = board[r + 1][c], board[r][c]
    # 가로 변경
    for r in range(n):
        for c in range(n-1):
            board[r][c],board[r][c+1]=board[r][c+1],board[r][c]
            #영향이 있었던 두 열에 대해서만 세로로 검사 c,c+1
            col_max(c)
            col_max(c+1)
            row_max(r)
            board[r][c], board[r][c + 1] = board[r][c + 1], board[r][c]

print(max_cnt)